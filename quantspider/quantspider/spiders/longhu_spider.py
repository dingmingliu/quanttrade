import scrapy
import datetime,time
from quantspider.items import QuantSpiderItem
__author__ = 'bett'
class AutoSpider(scrapy.Spider):
    name = "eastmoney"
    'http://data.eastmoney.com/stock/lhb/2015-04-08.html'
    allowed_domains = ["bitauto.com"]
    pre_url='http://car.bitauto.com'
    start_urls = [

    ]
    def __init__(self, category=None, *args, **kwargs):
        super(AutoSpider, self).__init__(*args, **kwargs)
        now=datetime.datetime.now()
        startDate=datetime.datetime.strptime('2006-03-29','%Y-%m-%d')
        day_count = (now - startDate).days + 1
        for single_date in [d for d in (startDate + datetime.timedelta(n) for n in range(day_count))]:
            datestr=datetime.datetime.strftime(single_date,'%Y-%m-%d')
            self.start_urls.append('http://data.eastmoney.com/stock/lhb/'+datestr+'.html')
    def parse(self, response):
        stock_tr=response.xpath("//table[@id='dt_1']/tbody/tr")
        for stock  in stock_tr:
            symbol=stock[1].xpath("a/text()")
            stockName=stock[2].xpath("a/text()").extract().encode('utf8')
            detailUrl=stock[3].xpath("a/@href")[0]
            zhangdie=stock[4].xpath("span/text()").extract()
            vol=stock[5].xpath("span/text()").extract()
            buy_val=stock[6].xpath("span/text()").extract()
            buy_rate=stock[7].xpath("span/text()").extract()
            sell_val=stock[8].xpath("span/text()").extract()
            sell_rate=stock[9].xpath("span/text()").extract()
            rason=stock[10].xpath("a/text()").extract().encode('utf8')
            request= scrapy.Request(detailUrl, callback=self.parseDetail)
            request.meta['item']={'symbol':symbol,'stockName':stockName,'zhangdie':zhangdie,
                                  'vol':vol,'buy_val':buy_val,'buy_rate':buy_rate,'sell_val':sell_val,'sell_rate':sell_rate,'rason':rason}
            yield request
    def parseDetail(self,response):
        tmp=response.meta['item']
        item =  QuantSpiderItem()
        item.symbol=tmp['symbol']
        item.stockName=tmp['stockName']
        item.zhangdie=tmp['zhangdie']
        item.vol=tmp['vol']
        item.buy_val=tmp['buy_val']
        item.buy_rate=tmp['buy_rate']
        item.sell_val=tmp['sell_val']
        item.sell_rate=tmp['sell_rate']
        item.rason=tmp['rason']
        salesDep=[]
        depTr=response.xpath("//table[@class='tab2']/tbody/tr")
        for dep in depTr:
            depName=dep.xpath("td")[1].xpath("a/text()").extract()
            buy_val=dep.xpath("td")[2].xpath("span/text()").extract()
            buy_rate=dep.xpath("td")[3].xpath("span/text()").extract()
            sell_val=dep.xpath("td")[4].xpath("span/text()").extract()
            sell_rate=dep.xpath("td")[5].xpath("span/text()").extract()
            net_amount=dep.xpath("td")[6].xpath("span/text()").extract()
            salesDep.append({'dep':depName,'buy_val':buy_val,'buy_rate':buy_rate,'sell_val':sell_val,'sell_rate':sell_rate,'net_amount':net_amount})
        return item





