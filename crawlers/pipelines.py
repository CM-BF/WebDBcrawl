# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class CrawlersPipeline(object):

    def __init__(self):
        self.file = open('item.json', 'wb')

    def process_item(self, item, spider):
        item_json = json.dump(dict(item)) + '\n'
        self.file.write(item_json)
        print('------------------------')
        return item
