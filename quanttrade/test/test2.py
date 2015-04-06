import numpy as np
import pandas as pd
import pandas.io.data as web
#goog=web.DataReader('GOOG',data_source='google',start='1/21/2013',end='4/6/2015')
goog=web.get_data_yahoo('000009.sz',start='1/21/2013',end='4/4/2015')
print goog.head()

