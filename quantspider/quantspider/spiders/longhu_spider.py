# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
import datetime,time
from quantspider.items import QuantSpiderItem
class AutoSpider(scrapy.Spider):
    name = "eastmoney"
    allowed_domains = ["data.eastmoney.com"]
    preurl='http://data.eastmoney.com/stock';
    start_urls = [
        'http://data.eastmoney.com/stock/lhb/2006-05-11.html'
    ]
    def __init__(self, category=None, *args, **kwargs):
        super(AutoSpider, self).__init__(*args, **kwargs)
        now=datetime.datetime.now()
        startDate=datetime.datetime.strptime('2006-03-29','%Y-%m-%d')
        day_count = (now - startDate).days + 1
        for single_date in [d for d in (startDate + datetime.timedelta(n) for n in range(day_count))]:
            week=int(time.strftime("%w"))
            log.msg("week :" + str(week))
            if week<=5:
                datestr=datetime.datetime.strftime(single_date,'%Y-%m-%d')
                self.start_urls.append('http://data.eastmoney.com/stock/lhb/'+datestr+'.html')

    def parse(self, response):
        log.msg('------------------')
        if response.xpath("//table[@id='dt_1']/tbody/tr/td/div/text()")[0].extract()==u'有相关数据...':
            log.msg('------------------no data')
            return
        else:
            log.msg('------------------have data'+response.url)
        stock_tr=response.xpath("//table[@id='dt_1']/tbody/tr[contains(@class,'all')]")
        date=response.url

        for stock  in stock_tr:
            stock_td=stock.xpath('td')
            log.msg('-----------'+stock_td[0].extract().encode('utf8'))
            symbol=stock_td[1].xpath("a/text()")[0].extract()
            stockName=stock_td[2].xpath("a/text()")[0].extract()
            detailUrl=stock_td[3].xpath("a/@href")[0].extract()
            zhangdie=stock_td[4].xpath("span/text()")[0].extract()
            vol=stock_td[5].xpath("span/text()")[0].extract()
            buy_val=stock_td[6].xpath("span/text()")[0].extract()
            buy_rate=stock_td[7].xpath("span/text()")[0].extract()
            sell_val=stock_td[8].xpath("span/text()")[0].extract()
            sell_rate=stock_td[9].xpath("span/text()")[0].extract()
            reason=stock_td[10].xpath("text()")[0].extract().encode('utf8')
            url=response.url
            request= scrapy.Request(self.preurl + detailUrl, callback=self.parseDetail)
            request.meta['item']={'symbol':symbol,'stockName':stockName,'zhangdie':zhangdie,
                                  'vol':vol,'buy_val':buy_val,'buy_rate':buy_rate,'sell_val':sell_val,
                                  'sell_rate':sell_rate,'reason':reason,'date':date[36:-5],'url':url}
            yield request
    def parseDetail(self,response):
        tmp=response.meta['item']
        item =  QuantSpiderItem()
        item['symbol']=tmp['symbol']
        item['stockName']=tmp['stockName']
        item['zhangdie']=tmp['zhangdie']
        item['vol']=tmp['vol']
        item['buy_val']=tmp['buy_val']
        item['buy_rate']=tmp['buy_rate']
        item['sell_val']=tmp['sell_val']
        item['sell_rate']=tmp['sell_rate']
        item['reason']=tmp['reason']
        item['date']=tmp['date']
        item['url']=tmp['url']
        item['depUrl']=response.url
        salesDep=[]
        depTr=response.xpath("//div[@id='cont1']/table[@class='tab2']/tbody/tr[contains(@onmouseout,'this.className')]")
        for dep in depTr:
            log.msg(dep.extract().encode('gb2312'))
            depTd=dep.xpath("td")
            depName=depTd[1].xpath("a/text()")[0].extract()
            buy_val=depTd[2].xpath("span/text()")[0].extract()
            buy_rate=depTd[3].xpath("span/text()")[0].extract()
            sell_val=depTd[4].xpath("span/text()")[0].extract()
            sell_rate=depTd[5].xpath("span/text()")[0].extract()
            net_amount=depTd[6].xpath("span/text()")[0].extract()
            salesDep.append({'depName':depName,'buy_val':buy_val,'buy_rate':buy_rate,'sell_val':sell_val,'sell_rate':sell_rate,'net_amount':net_amount})
        item['salesDep']=salesDep
        return item





