# -*- coding: utf-8 -*-
import scrapy
import logging
# from scrapy.utils.project import get_project_settings

logger = logging.getLogger(__name__)


class QbSpider(scrapy.Spider):
    name = 'qb'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # settings = get_project_settings()
        # MYSQL_HOST = settings.get("MYSQL_HOST")
        # print(MYSQL_HOST)

        # print(self.settings['MYSQL_HOST'], '*'*10)
        # print(self.settings['MYSQL_USER'], '*'*10)

        # print(id(self), 'qb')

        # print(self.hello)

        div_list = response.xpath('//div[@class="content"]/span')

        for div in div_list:
            item = {'username': div.xpath('../../../div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
                    # , 'content': div.xpath('../../../div[@class="author clearfix"]/a/img/@src').extract()
                    }
            # print(item)
            # logging.warning(item)
            yield item

        # next_url = response.xpath('//span[@class="next"]/../@href').extract_first()
        # # logging.warning(next_url)
        #
        # if next_url is not None:
        #     next_url = "https://www.qiushibaike.com" + next_url
        #     # logging.warning(next_url)
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )
