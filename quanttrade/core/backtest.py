__author__ = 'tyler'
from strategy import SMAStrategy
import pandas.io.data as web
import pandas.io.sql as psql

#coding=UTF8
class BackTest(object):
    def __init__(self):
        pass
    def run(self,s,data,initial_capital=100000.0):
        s.setup(data)
        #for day in data:
        s.run()


if(__name__=='__main__'):
    data=web.get_data_yahoo('000009.sz','3/1/2014','3/1/2015')

    smaStrategy=SMAStrategy(5,20);
    bt=BackTest()
    bt.run(smaStrategy,data)
