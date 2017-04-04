import scrapy

from qqnews.items import QqnewsItem

class DmozSpider(scrapy.Spider):
    name = "demo"
    #allowed_domains = ["dmoz.org"]
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
    	for question in response.xpath('//div[@class="question-summary"]'):
    		item = QqnewsItem()
        	item['title'] = question.xpath(".//div[@class='summary']/h3/a/text()").extract_first()
        	item['vote'] = question.xpath(".//div[@class='statscontainer']/div[@class='stats']/div[@class='vote']/div[@class='votes']/span/strong/text()").extract_first()
            #url =  question.xpath(".//div[@class='summary']/h3/a/@href").extract_first()
        	yield item

