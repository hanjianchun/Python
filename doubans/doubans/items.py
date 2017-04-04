# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubansItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DoubanBookItem(scrapy.Item):
	name = scrapy.Field()
	price = scrapy.Field()
	edition_year = scrapy.Field()
	publisher = scrapy.Field()
	ratings = scrapy.Field()

class DoubanMailItem(scrapy.Item):
	sender_time = scrapy.Field()
	sender_from = scrapy.Field()
	url = scrapy.Field()
	title = scrapy.Field()

class DoubanMovieCommentItem(scrapy.Item):
	useful_num = scrapy.Field()
	no_help_num = scrapy.Field()
	people = scrapy.Field()
	people_url = scrapy.Field()
	star = scrapy.Field()
	comment = scrapy.Field()
	title = scrapy.Field()
	comment_page_url = scrapy.Field()