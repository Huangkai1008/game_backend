# -*- coding: utf-8 -*-
import scrapy


class GameSpider(scrapy.Spider):
    name = 'game'
    allowed_domains = ['ali213.net']
    start_urls = ['http://ali213.net/']

    def parse(self, response):
        pass
