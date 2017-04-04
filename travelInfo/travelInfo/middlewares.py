# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy.http import HtmlResponse
from xml import etree
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import choice

from faker import Factory

f = Factory.create()


ua_list = [
    
]

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.resourceTimeout"] = 15
dcap["phantomjs.page.settings.loadImages"] = False
dcap["phantomjs.page.settings.userAgent"] = f.user_agent()#choice(ua_list)

#driver = webdriver.Firefox()
#driver = webdriver.Chrome()

class SelenimMiddleware(object):
    def process_request(self,request,spider):
        print "12333333"
        driver = webdriver.PhantomJS()

        if spider.name == 'Qua':
            try:
                driver.get(request.url)
                driver.implicity_wait(3)
                time.sleep(5)

                origin_page = driver.page_source #.decode('utf-8','ignore')
                origin_html = etree.HTML(origin_page)
                items = origin_html.xpath("//div[@class='m-fly-item s-oneway']")
                for index,item in enumerate(items):
                    flight_each = "//div[@id='list-box']/div["+str(index+1)+"]"
                    detail_span = "//div[@class='fl-detail-nav']/ul/li[1]/span[@class=]"
                    driver.find_element_by_xpath(flight_each+detail_span).click()

                true_page = driver.page_source
                driver.close
                return HtmlResponse(response.url,body = true_page,encoding = 'utf-8')
            except Exception, e:
                print "hello world exception"
                raise e
        elif spider.name=='Ctrip':
            driver.get(request.url)
            driver.implicity_wait(3)
            time.sleep(5)

            origin_page = driver.page_source #.decode('utf-8','ignore')
            origin_html = etree.HTML(origin_page)
            items = origin_html.xpath("//div[@id='J_flightlist2']/div")
            for index,item in enumerate(items):
                js = "var q=document.documentElemt.scrollTop=5000"
                driver.excute_script(js)
                time.sleep(2)

            true_page = driver.page_source
            driver.close
            return HtmlResponse(response.url,body = true_page,encoding = 'utf-8')

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TravelinfoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
