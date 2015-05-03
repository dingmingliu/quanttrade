# -*- coding: utf-8 -*-
__author__ = 'tyler'
import urllib2
import scrapy
from scrapy import log
import demjson

'''class AutoSpider(scrapy.Spider):
    name = "sse"
    allowed_domains = ["query.sse.com.cn"]
    preurl='http://data.eastmoney.com/stock';
    start_urls = [
        'http://query.sse.com.cn/infodisplay/showTradePublicFile.do?jsonCallBack=jQuery172023210379532913938_1430627585124&dateTx=2015-04-29&random=0.48195114223841695&_=1430627617454'
    ]
    def parse(self, response):
        jsonstr=response.body_as_unicode()
        log.msg(jsonstr[len('jQuery172023210379532913938_1430627585124'):-1])
        s1=demjson.decode(jsonstr[len('jQuery172023210379532913938_1430627585124('):-1])
        log.msg(s1['fileContents'])

if __name__=='__main__':'''


import re
tradeDay=''
send_headers = {
        'Host': 'query.sse.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.sse.com.cn/disclosure/diclosure/public/',
        'Connection': 'keep-alive'
    }
url='http://query.sse.com.cn/infodisplay/showTradePublicFile.do?jsonCallBack=jQuery172023210379532913938_1430627585124&dateTx=2015-04-29&random=0.48195114223841695&_=1430627617454'
req = urllib2.Request(url,headers=send_headers)
response = urllib2.urlopen(req)
html = response.read()
jsonStr=demjson.decode(html[len('jQuery172023210379532913938_1430627585124('):-1])
lines=jsonStr['fileContents']
def loopLineFun(lines):
    for line in lines:
        yield line.encode('utf8')
loopline=loopLineFun(lines)
class LHBItem():
    pass
dictlist = {}
r1 = re.compile(ur'\s+\(\d\)\s+(\d+)\s+([\u4e00-\u9fa5]+)\s+((-?\d+)(\.\d+)?)%\s+(\d+)\s+((-?\d+)(\.\d+)?)')
#r1 = re.compile(ur'\s+\(\d\)')

def readDep(loop,code):
    state='buy'
    rdep = re.compile(ur'\s+\(\d\)')
    rout=re.compile(ur'^\s?$')
    for tmp in loop:
        print tmp
        if tmp.find('买入营业部名称')>=0:
            state='buy'
            continue
        if tmp.find('卖出营业部名称')>=0:
            state='sell'
            continue
        outMatch=rout.match(tmp)
        if outMatch and state=='sell':
            print '跳出'
            return
        if rdep.match(tmp.decode('utf8')):
            dep=re.split('\s+',tmp)
            depName=dep[2]
            tradeAmount=dep[3]
            print 'depName ' + depName


r2=re.compile(ur'\s+[\u4e00-\u9fa5]+:\s(\d+)\s+[\u4e00-\u9fa5]+:\s[\u4e00-\u9fa5]+')
def readA7(loop):
    for tmp in loop:
        mat=r1.match(tmp.decode('utf8'))
        if mat:
            lbhItem =LHBItem()
            lbhItem.symbol= mat.group(1)
            lbhItem.stockName= mat.group(2)
            lbhItem.zhengdie= mat.group(3)
            lbhItem.vol=mat.group(6)
            lbhItem.amount= mat.group(7)
            dictlist[lbhItem.symbol]=lbhItem
            continue
        #dep
        mat2=r2.match(tmp.decode('utf8'))
        if mat2:
            print '*************************'
            readDep(loop,mat2.group(1))
        if tmp.find('二、')>=0:
            return


for tmp in loopline:
    print tmp
    if tmp.find('交易日期')>=0:
        tradeDay=tmp[13:]
        print tradeDay
    if tmp.find('偏离值达到7%')>=0:
        tmp=readA7(loopline)
        print tmp;
        break
    if tmp.find('二、')>=0:
        print '-------'
for k in dictlist:
    print k

