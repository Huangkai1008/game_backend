# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GameScrapyItem(scrapy.Item):
    """
    游戏信息爬虫
    """
    name = scrapy.Field()
    foreign_name = scrapy.Field()
    language = scrapy.Field()
    tags = scrapy.Field()
    company = scrapy.Field()
    type = scrapy.Field()
    desc = scrapy.Field()

