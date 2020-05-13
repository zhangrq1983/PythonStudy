# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging

# logger = logging.getLogger()
logger = logging.getLogger(__name__)


class MyspiderPipeline:

    # def open_spider(self, spider):
    #     spider.hello = 'world'

    def process_item(self, item, spider):

        # print(spider.settings.get("MYSQL_HOST"), '*' * 10)
        # print(spider.settings.get('MYSQL_USER'), '*' * 10)

        # print(id(spider), 'pipelines')

        item['hello'] = 'world'
        # print('qb' + str(item))
        logger.warning(item)
        return item


# class MyspiderPipeline1:
#     def process_item(self, item, spider):
#         print('jd' + str(item))
#         return item