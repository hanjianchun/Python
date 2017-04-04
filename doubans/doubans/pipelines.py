# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubansPipeline(object):
    def process_item(self, item, spider):
        return item

class DoubanBookPipline(object):
	def process_item(self,item,spider):
		info = item['price'].split(' / ')
		item['name'] = item['name']
		return item
