# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class YgcSpider(CrawlSpider):
    name = 'ygc'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    rules = (
        Rule(LinkExtractor(allow=r'/political/politics/index\?id=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/political/index/politicsNewest\?id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        content = response.xpath('//pre//text()').get()
        item['content'] = content

        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        # print(item)
        # return item

        yield item
