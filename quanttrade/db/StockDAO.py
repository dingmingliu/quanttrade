__author__ = 'tyler'
#coding=UTF8
import mysql
from mysql import connector
from config import *
class StockDAO(object):
    '股票代码相关操作'
    def __init__(self):
        self.cnx = mysql.connector.connect(**db_config)
        self.__cursor =  self.cnx.cursor()
    def getAllSymbols(self):
        self.__cursor =  self.cnx.cursor()
        self.__cursor.execute('select symbol,name FROM tbl_stock where source=%s',('yahoo',))
        allSymbols= self.__cursor.fetchall()
        return allSymbols
    def batchInsert(self,data):
        self.__cursor =  self.cnx.cursor()
        sql ='insert into tbl_historical(symbol,open,high,low,close,volume,date) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        self.__cursor.executemany(sql,data)
        self.__cursor.close();
        self.cnx.commit()
    def getStartDate(self,symbol):
        self.__cursor =  self.cnx.cursor()
        self.__cursor.execute('select max(date) FROM tbl_historical where symbol=%s',(symbol,))
        start_date= self.__cursor.fetchone()[0]
        self.__cursor.close();
        return start_date
    def updateSource(self,symbol,source):
        self.__cursor =  self.cnx.cursor()
        self.__cursor.execute('update tbl_stock set source=%s where symbol=%s ',(source,symbol))
        self.cnx.commit()
        self.__cursor.close();
 #   def __del__(self):
#        self.cnx.close();



