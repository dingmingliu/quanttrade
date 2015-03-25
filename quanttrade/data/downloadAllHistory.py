__author__ = 'tyler'
import mysql
from mysql import connector
from  datetime  import  *
import ystockquote
user = 'root'
pwd = 'root'
host = '192.8.19.44'
db = 'quanttrade'
cnx = mysql.connector.connect(user=user, password=pwd, host=host,database=db)
cursor = cnx.cursor()
cursor.execute("select * FROM tbl_stock");
for symbol,name in cursor:
    prices=ystockquote.get_historical_prices(symbol, '1990-01-01', datetime.today())
    for date in prices.keys():
        open=(float(prices[date]['Open']))
        high=(float(prices[date]['High']))
        low=(float(prices[date]['Low']))
        close=(float(prices[date]['Close']))
        volume=(float(prices[date]['Volume']))
        adj_close=float(prices[date]['Adj Close'])
        sql ="insert into tbl_historical(symbol,open,high,low,+close,volume+,adjClose) VALUES ('+symbol+','+open+','+high+','+low+','+close+','+volume+','+adj_close+')"
        print(sql)
        cursor.execute(sql);


