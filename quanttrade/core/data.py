__author__ = 'bett'
import MySQLdb as db
import pandas.io.sql as psql
from config import db_config
def getData(symbols,start,end):
    database = db.connect(**db_config)
    data=psql.frame_query("SELECT * FROM tbl_historical where start", database)
    return data;
if(__name__=='__main__'):
    getData('000009.sz','2013-1-1','2015-4-8')
