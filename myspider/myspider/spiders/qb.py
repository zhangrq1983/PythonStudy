# -*- coding: utf-8 -*-
import scrapy


class QbSpider(scrapy.Spider):
    name = 'qb'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):

        div_list = response.xpath('//div[@class="content"]/span')

        for div in div_list:
            item = {'username': div.xpath('../../../div[@class="author clearfix"]/a[2]/h2/text()').extract_first(),
                    'content': div.xpath('../../../div[@class="author clearfix"]/a/img/@src').extract()}
            # print(item)
            yield item


