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

#if 600  append .ss    300 and 000 .sz
def getSymbol(code):
    if(code.startswith('600')):
        return code+'.ss';
    elif(code.startswith('300') or code.startswith('00')):
        return code+'.sz'
    else:
        print('code not found ' + code)


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
cursor.execute("select symbol,name FROM tbl_stock")
allSymbols=cursor.fetchall()

for symbol,name in allSymbols:
    fSymbol=getSymbol('600109')
    cursor.execute('select max(date) FROM tbl_historical where symbol="600109.ss"',(fSymbol))
    start_date=cursor.fetchone()[0]
    prices=ystockquote.get_historical_prices(fSymbol, '1990-01-01', datetime.today().strftime('%Y-%m-%d'))
    data=[]
    for date in prices.keys():
        open=(float(prices[date]['Open']))
        high=(float(prices[date]['High']))
        low=(float(prices[date]['Low']))
        close=(float(prices[date]['Close']))
        volume=(float(prices[date]['Volume']))
        adj_close=float(prices[date]['Adj Close'])
        sql ='insert into tbl_historical(symbol,open,high,low,close,volume,date) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        params=(fSymbol,open,high,low,close,volume,date)
        data.append(params)
    cursor.executemany(sql,data)
    cnx.commit()
cursor.close()
cnx.close;


