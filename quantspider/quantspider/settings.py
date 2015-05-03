# -*- coding: utf-8 -*-

# Scrapy settings for quantspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'quantspider'
DOWNLOAD_DELAY=1
LOG_ENCODING='gb2312'
DEFAULT_REQUEST_HEADERS={
        'Host': 'query.sse.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.sse.com.cn/disclosure/diclosure/public/',
        'Connection': 'keep-alive'
    }
SPIDER_MODULES = ['quantspider.spiders']
NEWSPIDER_MODULE = 'quantspider.spiders'
ITEM_PIPELINES = {
    'quantspider.pipelines.StoreItem': 300,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'quantspider (+http://www.yourdomain.com)'
