import scrapy

from meitu.items import MeituItem
from faker import Factory
f = Factory.create()

class meituSpider(scrapy.Spider):
	name = "meituSpider"
	start_urls = ['http://www.meizitu.com/a/list_1_1.html']
	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.01',
		'Accept-Encoding':'gzip,deflate,br',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Connection':'keep-alive',
		'User-Agent':f.user_agent()
	}

	def start_requests(self):

		urls = ['http://www.meizitu.com/a/list_1_%s.html' %s for s in range(1,10)]
		for url in urls:
			yield scrapy.Request(url=url,headers = self.headers,meta={'cookiejar':1},
							callback=self.parse_test)

	def parse_test(self,response):
		page_urls = response.xpath('//div[@class="con"]//div[@class="pic"]//a//@href').extract()
		for page_url in page_urls:
			yield scrapy.Request(page_url,headers = self.headers,callback=self.parse_page)
	
	def parse_page(self,response):
		image_urls = response.xpath('//div[@id="picture"]//p//img//@src').extract()
		item = MeituItem()
		item['image_urls'] = image_urls
		yield item
			
			