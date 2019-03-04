# -*- coding: utf-8 -*-
import scrapy

from game_scrapy.items import GameScrapyItem


class GameSpider(scrapy.Spider):
    name = 'game'
    allowed_domains = ['gamersky.com']
    start_urls = ['https://www.gamersky.com/z/darksouls3/']

    def parse(self, response):
        game = response.xpath('//div[@class="gameinfor"]/div[@class="gamecon"]')

        item = GameScrapyItem()
        game_title = game.xpath('./div[@class="gametit"]')
        item['name'] = game_title.xpath('./div[@class="CHtit"]//text()').extract_first()
        item['foreign_name'] = game_title.xpath('./div[@class="ENtit"]//text()').extract_first()

        game_infos = game.xpath('./ul[@class="YXXX"]//li')

        game_dict = {g.xpath('./div[@class="u1"]//text()').extract_first():
                         g.xpath('./div[@class="u2"]//text()').extract_first() for g in game_infos}

        item['type'] = game_dict['游戏类型：']
        item['company'] = game_dict['游戏制作：']

        item['desc'] = response.xpath('//div[@class="gameinfor"]/div[@class="profile"]/div/p[last()]//text()'). \
            extract_first()

        yield item
