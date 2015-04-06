from data.YahooDLThread import YahooDLThread
import  Queue
__author__ = 'tyler'

from db.StockDAO import StockDAO
import logging,os
import logging.config

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("example02")

class YahooFinance(object):
    def __init__(self):
        self.q=Queue.Queue()
        self.stockDao= StockDAO()
    def downAllStock(self):
        allSymbol=self.stockDao.getAllSymbols()
        for symbol,name in allSymbol:
            self.q.put(symbol)
        logging.info('total symbol count is : %s ',len(allSymbol))
        for i in range(2):
            t=YahooDLThread(self.q)
            t.start();


if(__name__ == '__main__'):
    a = YahooFinance()
    #print(a.getYahooSymbol('000001'))

