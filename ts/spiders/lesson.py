# -*- coding: utf-8 -*-
import scrapy
from ts.items import TsItem
from scrapy.http import Request

class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['http://www.hellobi.com/']

    #response为starturl爬取后的结果，接下来只需要对爬取下来的结果进行分析即可。
    def parse(self, response):

        item = TsItem()
        item['title'] = response.xpath("//ol[@class='breadcrumb']/li[@class='active']/text()").extract()
        item['link'] = response.xpath("//ul[@class='nav nav-tabs']/li[@class='active']/a/@href").extract()
        item['stu'] = response.xpath("//span[@class='course-view']/text()").extract()
        yield item
        for i in range(1, 235):
            url = "https://edu.hellobi.com/course/"+str(i)
            yield Request(url, callback=self.parse)




