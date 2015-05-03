__author__ = 'tyler'
from sqlalchemy.databases import mysql
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'root',
    'db':'quanttrade',
    'charset':'utf8'
}

engine = create_engine('mysql://%s:%s@%s/%s?charset=%s'%(db_config['user'],
                                                     db_config['passwd'],
                                                     db_config['host'],
                                                     db_config['db'],
                                                     db_config['charset']), echo=True)
metadata = MetaData()
longhuTable=Table('TBL_LONGHU', metadata,
    Column('id', Integer, primary_key=True),
    Column('symbol', String(50)),
    Column('stockName', String(50)),
    Column('zhangdie', String(50)),
    Column('vol', String(50)),
    Column('buy_val', String(50)),
    Column('buy_rate', String(50)),
    Column('sell_val', String(50)),
    Column('sell_rate', String(50)),
    Column('reason', String(50)),
    mysql_engine='InnoDB',
    mysql_charset='utf8'
)
metadata.create_all(engine)
class LongHu(object):
    pass

mapper(LongHu, longhuTable)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
def insert():
    longhu = LongHu()
    longhu.id=1
    session.add(longhu)
    session.flush()
    session.commit()

