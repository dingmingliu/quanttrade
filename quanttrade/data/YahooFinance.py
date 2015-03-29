import threading
from urllib.error import HTTPError
from mysql.connector.errors import DataError
__author__ = 'tyler'
import ystockquote,datetime
from db.StockDAO import StockDAO
import logging,os
format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), format=format,
                    level = logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

class YahooFinance(object):
    def __init__(self):
        self.stockDao= StockDAO()
    def downAllStock(self):
        allSymbol=self.stockDao.getAllSymbols()
        logging.info('total symbol count is : %s ',len(allSymbol))
        threading.thread
    def downLoad(self):
        for symbol,name in allSymbol:
            logging.info('come to download symbol : %s ,%s ',symbol,name )
            data_startDate=self.stockDao.getStartDate(symbol)
            today=datetime.date.today()
            '初始化开始时间'
            if(data_startDate == None):
                startDate='1990-01-01'
            else:
                startDate=data_startDate + datetime.timedelta(days = 1)
                if(startDate > today):
                    logging.info('已存在数据')
                    continue
                elif(startDate==today and startDate.weekday()>5):
                    logging.info('not a work day')
                    continue
                elif(startDate<today and  startDate.weekday()>=5 and today.weekday()>=5):
                    logging.info('周末不用执行')
                    continue
                startDate=startDate.strftime('%Y-%m-%d')

            endDate=today.strftime('%Y-%m-%d')
           # logging.info('download symbol  : %s' , symbol)
            logging.info('download symbol %s name %s startdate %s enddate %s: ',symbol,name,startDate,endDate)
            data=self.downStock(symbol,startDate,endDate)
            if(data==None):
                continue
            logging.info('data size symbol %s %s %s: ',symbol,name,len(data) )
            self.stockDao.batchInsert(data)
            logging.info('finish download symbol %s %s : ',symbol,name )
    def downStock(self,symbol,startDate,endDate):
        tmpSymbol=self.getYahooSymbol(symbol)
        try:
            prices=ystockquote.get_historical_prices(tmpSymbol,startDate, endDate)
            data=[]
            for date in prices.keys():
                open=(float(prices[date]['Open']))
                high=(float(prices[date]['High']))
                low=(float(prices[date]['Low']))
                close=(float(prices[date]['Close']))
                volume=(float(prices[date]['Volume']))
                adj_close=float(prices[date]['Adj Close'])
                sql ='insert into tbl_historical(symbol,open,high,low,close,volume,date) VALUES (%s,%s,%s,%s,%s,%s,%s)'
                params=(symbol,open,high,low,close,volume,date)
                data.append(params)
            return data
        except HTTPError as e:
            logging.warning('yahoo 没有这只股票 %s',e)
            if(404==e.getcode()):
                '标致yahoo没有改股票的数据'
                self.stockDao.updateSource(symbol,'wind')
        except DataError as ex:
            logging.warning(ex)

    #if 600  append .ss    300 and 000 .sz
    def getYahooSymbol(self,code):
        if(code.startswith('600')):
            return code+'.ss';
        elif(code.startswith('300') or code.startswith('00')):
            return code+'.sz'
        else:
            print('code not found ' + code)
if(__name__ == '__main__'):
    a = YahooFinance()
    print(a.getYahooSymbol('000001'))

