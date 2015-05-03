# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import pymongo
from pymongo import MongoClient
from scrapy import log
class StoreItem(object):
    def process_item(self, item, spider):
        client = MongoClient()
        db = client['quant']
        collection = db['lhb']
        post = {"symbol": item['symbol'], "stockName":item['stockName'],"zhangdie":item['zhangdie'].replace('%',''),
                "vol":item['vol'],"buy_val":item['buy_val'],"buy_rate":item['buy_rate'].replace('%',''),
                "sell_val":item['sell_val'],"sell_rate":item['sell_rate'].replace('%',''),"reason":item['reason'],
                "date":item['date'],"url":item['url'],"['depUrl']":item['depUrl'],
                "tradeDeps":[ {"name":depTmp['depName'],"buy_val":depTmp['buy_val'],"buy_rate":depTmp['buy_rate'],
                               "sell_val":depTmp['sell_val'],"sell_rate":depTmp['sell_rate'],"net_amount":depTmp['net_amount']} for depTmp in item['salesDep']]
        }

        collection.insert(post)











