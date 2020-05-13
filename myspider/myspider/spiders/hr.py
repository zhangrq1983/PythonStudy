# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']
    # start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        # div_list = response.xpath('//div[@class="recruit-wrap recruit-margin"]')
        div_list = response.xpath('//body/div/div[4]/div[3]/div[2]/div[2]/div')


        for div in div_list:
            item = {'title': div.xpath('./td/a/text()').extract_first()
                    , 'capt': div.xpath('/td[2]/text()').extract_first()
                    , 'publist_date': div.xpath('/td[last()]/text()').extract_first()
                    }
            logger.warning(item)
            yield item

            next_url = response.xpath('//a[@id="next"]/@href').extract_first()

            if next_url != 'javascript:;':
                next_url = "https://careers.tencent.com/search.html?index=" + next_url
                yield scrapy.Request(
                    next_url,
                    callback=self.parse,
                    meta={"item", item}
                )


    def parse1(self, response):
        item = response.meta['item']
        print(item)
