# -*- coding:utf-8 -*-

import scrapy
from faker import Factory
from doubans.items import DoubanMovieCommentItem
import urlparse
f = Factory.create()

class DoubanCommontSpider(scrapy.Spider):
	name = 'douban_comment'
	start_urls = [
		'https://www.douban.com'
	]

	headers = {
      	#"Host":"accounts.douban.com",
      	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
      	"Accept-Encoding":"gzip, deflate",
      	#"Referer":"http://onlinelibrary.wiley.com/journal/10.1002/(ISSN)1521-3773",
      	#"Cookie":"EuCookie='this site uses cookies'; __utma=235730399.1295424692.1421928359.1447763419.1447815829.20; s_fid=2945BB418F8B3FEE-1902CCBEDBBA7EA2; __atuvc=0%7C37%2C0%7C38%2C0%7C39%2C0%7C40%2C3%7C41; __gads=ID=44b4ae1ff8e30f86:T=1423626648:S=ALNI_MalhqbGv303qnu14HBk1HfhJIDrfQ; __utmz=235730399.1447763419.19.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; TrackJS=c428ef97-432b-443e-bdfe-0880dcf38417; OLProdServerID=1026; JSESSIONID=441E57608CA4A81DFA82F4C7432B400F.f03t02; WOLSIGNATURE=7f89d4e4-d588-49a2-9f19-26490ac3cdd3; REPORTINGWOLSIGNATURE=7306160150857908530; __utmc=235730399; s_vnum=1450355421193%26vn%3D2; s_cc=true; __utmb=235730399.3.10.1447815829; __utmt=1; s_invisit=true; s_visit=1; s_prevChannel=JOURNALS; s_prevProp1=TITLE_HOME; s_prevProp2=TITLE_HOME",
      	"Connection":"keep-alive",
      	#"Origin":"https://accounts.douban.com",
      	"User-Agent":f.user_agent()
    }

	formdata = {
		'form_email':'1452202397@qq.com',
		'form_password':'I9494941',
		'login':'登录',
		'redir':'https://www.douban.com/',
		'source':'None'
	}

	def start_requests(self):
		print 'srart '
		return [scrapy.Request(url=r'https://www.douban.com/accounts/login',headers = self.headers,meta={'cookiejar':1},
							callback=self.parse_login)]


	def parse_login(self,response):
		print "login==="
		print response.meta
		if 'captcha_image' in response.body:
			print 'Copy the link:'
			link = response.xpath('//img[@class="captcha_image"]/@src').extract()[0]
			print link
			code = raw_input("captcha_solution:")
			captcha_id = urlparse.parse_qs(urlparse.urlparse(link).query,True)['id'][0]
			self.formdata['captcha_solution'] = code
			self.formdata['captcha_id'] = captcha_id
		return [scrapy.FormRequest.from_response(response,formdata=self.formdata,headers=self.headers,meta={'cookiejar':response.meta['cookiejar']},
			callback=self.after_login)]

	def after_login(self,response):
		self.headers['Host'] = "www.douban.com"
		yield scrapy.Request(url = 'https://movie.douban.com/subject/1292063/reviews',
								meta={'cookiejar':response.meta['cookiejar']},
								headers = self.headers,
								callback = self.parse_comment_url)
		yield scrapy.Request(url = 'https://movie.douban.com/subject/1292063/reviews',
								meta={'cookiejar':response.meta['cookiejar']},
								headers = self.headers,
								callback = self.parse_next_page,
								dont_filter = True)

	def parse_next_page(self,response):
	
		try:
			next_url = response.urljoin(response.xpath('//span[@class="next"]/a/@href').extract_first())
			print "下一页"
			print next_url
			yield scrapy.Request(url=next_url,
								meta = {'cookiejar':response.meta['cookiejar']},
								headers = self.headers,
								callback = self.parse_comment_url,
								dont_filter = True)
			yield scrapy.Request(url=next_url,
								meta = {'cookiejar':response.meta['cookiejar']},
								headers = self.headers,
								callback = self.parse_next_page,
								dont_filter = True)
		except Exception, e:
			raise e

	def parse_comment_url(self,response):
		for body in response.xpath('//div[@class="main review-item"]'):
			comment_url = body.xpath('header/h3[@class="title"]/a/@href').extract_first()
			yield scrapy.Request(url = comment_url,
								meta = {'cookiejar':response.meta['cookiejar']},
								headers = self.headers,
								callback = self.parse_comment)
			# yield scrapy.Request(url = comment_url,
			# 					meta = {'cookiejar':response.meta['cookiejar']},
			# 					headers = self.headers,
			# 					callback = self.parse_comment_url,
			# 					dont_filter = True)
	
	def parse_comment(self,response):
		print "jinru comment"
		commentItem = DoubanMovieCommentItem()
		commentItem["comment"] = response.xpath('//*[@id="link-report"]/div/text()').extract()[0]
		yield commentItem
		
