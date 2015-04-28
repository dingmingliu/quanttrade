# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuantSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol=scrapy.Field()
    stockName=scrapy.Field()
    zhangdie=scrapy.Field()
    vol=scrapy.Field()
    buy_val=scrapy.Field()
    buy_rate=scrapy.Field()
    sell_val=scrapy.Field()
    sell_rate=scrapy.Field()
    rasion=scrapy.Field()


