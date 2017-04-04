# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

 class FindSctripItem(scrapy.Item):
  	site = scrapy.Field()
 	company = scrapy.Field()
