#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:08:53 2017
网络爬虫实例  scrapy runspider xpath_pachong.py -o result.json
@author: hanjianchun
"""
#1.抓一页
import scrapy

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    #初始网站
    start_urls  = ['http://stackoverflow.com/questions?sort=votes']
    def parse(self,response):
        for question in response.xpath('//div[@class="question-summary"]'):
            title = question.xpath(".//div[@class='summary']/h3/a/text()").extract_first()
            vote = question.xpath(".//div[@class='statscontainer']/div[@class='stats']/div[@class='vote']/div[@class='votes']/span/strong/text()").extract_first()
            url =  question.xpath(".//div[@class='summary']/h3/a/@href").extract_first()
            yield{
                    "title":title,
                    "vote":vote,
                    "url":url
            }
