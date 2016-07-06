# -*- coding: utf-8 -*-

import sqlite3,sys

num = 1
conn = sqlite3.connect('E:\pycharmprojects\location.db')
cursor = conn.cursor()
conn.row_factory = sqlite3.Row
# cursor.execute("select * from location_specific where num != lat")
cursor.execute("select num,id, ip,lat,lng,radius  from ip2location3306 ")
rows = cursor.fetchall()

file = open('E:\pycharmprojects\dbsample1\data\location3306full.txt','a')            #写入txt文本

for row in rows:
    if row[0] != row[3]:
        file.write("{\"lat\":%s ,\"lng\": %s,\"id\":%s,\"radius\":%s},"%(row[3], row[4],row[1],row[5]))
        print num
        num = num + 1

cursor.close()
conn.close()