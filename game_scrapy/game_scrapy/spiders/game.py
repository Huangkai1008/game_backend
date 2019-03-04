# -*- coding: utf-8 -*-
import scrapy

from game_scrapy.items import GameScrapyItem


class GameSpider(scrapy.Spider):
    name = 'game'
    allowed_domains = ['ali213.net']
    start_urls = ['http://0day.ali213.net/html/2017/30225.html']

    def parse(self, response):
        game = response.xpath('//div[@class="xs-top"]//div[@class="xs-c1-c"]')

        item = GameScrapyItem()
        item['name'] = game.xpath('./h1[@class="xs-c1-c-cn"]/span//text()').extract_first()
        item['foreign_name'] = game.xpath('./h2[@class="xs-c1-c-en"]//text()').extract_first()

        game_info = game.xpath('./div[@class="xs-c1-c-info"]')
        item['type'] = game_info.xpath('./div[@class="xs-c1-c-info-l]//text()').extract_first()

        yield item
