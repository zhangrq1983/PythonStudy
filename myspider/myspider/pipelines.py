# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging

# logger = logging.getLogger()
logger = logging.getLogger(__name__)


class MyspiderPipeline:
    def process_item(self, item, spider):
        item['hello'] = 'world'
        # print('qb' + str(item))
        logger.warning(item)
        return item


# class MyspiderPipeline1:
#     def process_item(self, item, spider):
#         print('jd' + str(item))
#         return item