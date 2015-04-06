__author__ = 'tyler'
from strategy import SMAStrategy
#coding=UTF8
class BackTest(object):
    def __init__(self):
        pass
    def run(self,s,data):

        #初始化策略
        #loop day
        s.run()

if(__name__=='__main__'):
    smaStrategy=SMAStrategy();
    bt=BackTest(smaStrategy)
    bt.run()
