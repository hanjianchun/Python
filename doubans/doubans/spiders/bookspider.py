# -*- coding:utf-8 -*-

import scrapy
from faker import Factory
from doubans.items import DoubanBookItem
import urlparse
f = Factory.create()


class BookSpider(scrapy.Spider):
	name = 'doubanbook'
	#allowed_domains = ['book.douban.com']
	start_urls = ['https://book.douban.com/top250/']

	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.01',
		'Accept-Encoding':'gzip,deflate,br',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Connection':'keep-alive',
		'Host':'book.douban.com',
		'User-Agent':f.user_agent()
	}

	def start_requests(self):
		print "start request"
		return [scrapy.Request(url='https://book.douban.com/top250/',headers = self.headers,meta={'cookiejar':1},
							callback=self.parse_test)]

	def parse_test(self,response):
		print response.url
		
		#请求第一页
		yield scrapy.Request(response.url,headers = self.headers,callback=self.parse_next)
		#请求其他页
		for page in response.xpath("//div[@class='paginator']/a"):
			link = page.xpath('@href').extract()[0]
			print link
			yield scrapy.Request(link,headers = self.headers,callback=self.parse_next)

	def parse_next(self,response):
		print "enter next!"
		for item in response.xpath("//tr[@class='item']"):
			book = DoubanBookItem()
			book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
			book['price'] = item.xpath('td[2]/p/text()').extract()[0]
			book['ratings'] = item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
			yield book