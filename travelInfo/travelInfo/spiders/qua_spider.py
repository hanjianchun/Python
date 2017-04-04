# -*- coding: utf-8 -*-

import scrapy

#from travelInfo.items import FindSctripItem

class QuaSpider(scrapy.Spider):
	name = 'Qua'
	start_urls = [
		'http://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=北京&searchArrivalAirport=上海&searchDepartureTime=2017-04-06&searchArrivalTime=2017-04-09&nextNDays=0&startSearch=true&fromCode=BJS&toCode=SHA&from=flight_dom_search&lowestPrice=null'
	]

	def parse(self,response):
		print response.body