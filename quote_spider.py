#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:10:07 2017

@author: hanjianchun
"""
import scrapy

class quoteSpider(scrapy.Spider):
    name = 'quote'
    #初始网站
    start_urls  = ['http://quote.toscrape.com/tag/humor/']
    def parse(self,response):
        for question in response.xpath('//div[@class="quote"]'):
            title = question.xpath(".//div[@class='summary']/h3/a/text()").extract_first()
            vote = question.xpath(".//div[@class='statscontainer']/div[@class='stats']/div[@class='vote']/div[@class='votes']/span/strong/text()").extract_first()
            url =  question.xpath(".//div[@class='summary']/h3/a/@href").extract_first()
            yield{
                    "title":title,
                    "vote":vote,
                    "url":url
            }
            
            next_page = respnse.xpath('.//li[@href]')
            if next_path is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page,callback=self.parse)





