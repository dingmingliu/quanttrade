__author__ = 'tyler'
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import bt
data = bt.get('spy,agg', start='2010-01-01')
s = bt.Strategy('s1', [bt.algos.RunMonthly(),
                       bt.algos.SelectAll(),
                       bt.algos.WeighEqually(),
                       bt.algos.Rebalance()])
# create a backtest and run it
test = bt.Backtest(s, data)
res = bt.run(test)
res.plot()
res.display()
res.plot_histogram()