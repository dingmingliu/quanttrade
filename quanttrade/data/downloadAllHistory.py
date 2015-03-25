__author__ = 'tyler'
import mysql
from mysql import connector
from  datetime  import  *
import ystockquote
config={'user' : 'root',
        'password' : 'root',
        'host' : 'localhost',
        'database':'quanttrade',
        'charset':'utf8'
        }

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
cursor.execute("select symbol,name FROM tbl_stock");
#for symbol,name in cursor:
prices=ystockquote.get_historical_prices('600993', '1990-01-01', datetime.today())
for date in prices.keys():
        open=(float(prices[date]['Open']))
        high=(float(prices[date]['High']))
        low=(float(prices[date]['Low']))
        close=(float(prices[date]['Close']))
        volume=(float(prices[date]['Volume']))
        adj_close=float(prices[date]['Adj Close'])
        sql ='insert into tbl_historical(symbol,open,high,low,close,volume,adjClose) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        params=('600109',open,high,low,close,volume,adj_close)
        cursor.execute(sql,params)
cnx.commit()

