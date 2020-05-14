# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        cookies = ""
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}


    def parse(self, response):
        pass
