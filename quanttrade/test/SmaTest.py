__author__ = 'tyler'
import bt
#%pylab inline
# download data
data = bt.get('aapl,msft', start='2013-01-01')
data.head()
import pandas as pd
# a rolling mean is a moving average, right?
sma = pd.rolling_mean(data, 50)
s = bt.Strategy('above50sma', [ bt.algos.SelectWhere(data > sma),
                               bt.algos.WeighEqually(),
                               bt.algos.Rebalance()])

# now we create the Backtest
t = bt.Backtest(s, data)

# and let's run it!
res = bt.run(t)

