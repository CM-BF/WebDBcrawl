# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sent = scrapy.Field()  # 开始日期
    type = scrapy.Field()  # 发布类型
    author = scrapy.Field()  # 来自
    subject = scrapy.Field()  # 计划
    content = scrapy.Field()
    url = scrapy.Field()
    deadline = scrapy.Field() # 期限
    webpage =  scrapy.Field() # 主页
