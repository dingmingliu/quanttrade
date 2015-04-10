import pandas as pd
import numpy as np
import cython as cy

#coding=UTF8
class Strategy(object):
    _capital = cy.declare(cy.double)
    _net_flows = cy.declare(cy.double)
    _last_value = cy.declare(cy.double)
    _last_price = cy.declare(cy.double)
    _last_fee = cy.declare(cy.double)
    def run(self):
        pass
    def setup(self,data):
        self.data=data
    @property
    def values(self):
        if self.root.stale:
            self.root.update(self.now, None)
        return self._values.ix[:self.now]


class SMAStrategy(Strategy):
    def __init__(self,short,long):
        self.short=short
        self.long=long
    def run(self):
        short_avg=pd.rolling_mean(self.data,self.short)
        long_avg=pd.rolling_meam(self.data,self.long)
        print(short_avg)
        for day in self.data.index:
            pass
        print(self.data[day])
        '''if(self.short_avg[]>self.long_avg):
            pass
        else:
            pass'''