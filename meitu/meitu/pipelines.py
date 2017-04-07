# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from meitu import settings
import os
from faker import Factory
f = Factory.create()

class MeituPipeline(object):
    def process_item(self, item, spider):
    	if 'image_urls' in item:#如何‘图片地址’在项目中
            images = []#定义图片空集
            
            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)
            print(dir_path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for image_url in item['image_urls']:
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True,headers={
												'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.01',
												'Accept-Encoding':'gzip,deflate,br',
												'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
												'Connection':'keep-alive',
												'User-Agent':f.user_agent()
											})
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)
    	return item

