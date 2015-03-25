import mysql
from mysql import connector
config={'user' : 'root',
        'password' : 'root',
        'host' : '192.8.19.44',
        'database':'quanttrade',
        'charset':'utf8'
        }

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
file_object = open('d:/Table.txt','r',encoding='utf-8')
sql='insert into tbl_stock(symbol,name) values(%s,%s)'
try:
    list_of_all_the_lines = file_object.readlines( )
    for line in list_of_all_the_lines:
        data=(line[2:8],line[9:])
        print(data)
        cursor.execute(sql,data);
        cnx.commit();
finally:
    file_object.close( )
cnx.close()



