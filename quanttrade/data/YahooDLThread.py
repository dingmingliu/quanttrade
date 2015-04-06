__author__ = 'tyler'
#coding=UTF8
import threading
import logging,os
import ystockquote,datetime
from urllib2 import HTTPError
from mysql.connector.errors import DataError
from db.StockDAO import StockDAO
import logging.config

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("example02")

class YahooDLThread(threading.Thread ):
    def __init__(self,q):
        threading.Thread.__init__(self)
        self.stockDao= StockDAO()
        self.q=q
    def run(self):
        while self.q.not_empty:
            symbol=self.q.get()
            logging.info('come to download symbol : %s ',symbol )
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
            logging.info('download symbol %s startdate %s enddate %s: ',symbol,startDate,endDate)
            data=self.downStock(symbol,startDate,endDate)
            if(data==None):
                continue
            logging.info('data size symbol %s %s: ',symbol,len(data) )
            self.stockDao.batchInsert(data)
            logging.info('finish download symbol %s : ',symbol)


    def downStock(self,symbol,startDate,endDate):
         #if 600  append .ss    300 and 000 .sz

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

    def getYahooSymbol(self,code):
        if(code.startswith('600')):
            return code+'.ss';
        elif(code.startswith('300') or code.startswith('00')):
            return code+'.sz'
        else:
            print('code not found ' + code)


