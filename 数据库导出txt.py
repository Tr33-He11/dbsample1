# -*- coding: utf-8 -*-

import sqlite3,sys

num = 1
conn = sqlite3.connect('E:\pycharmprojects\location.db')
cursor = conn.cursor()
conn.row_factory = sqlite3.Row
# cursor.execute("select * from location_specific where num != lat")
cursor.execute("select num,id, ip,lat,lng,min(radius),radius  from ip2location3506 group by id ")
rows = cursor.fetchall()

file = open('E:\pycharmprojects\dbsample1\data\location3506.txt','a')            #写入txt文本

for row in rows:
    if row[0] != row[3]:
        file.write("{\"lat\":%s ,\"lng\": %s,\"id\":%s,\"radius\":%s},"%(row[3], row[4],row[1],row[6]))
        print num
        num = num + 1

cursor.close()
conn.close()


# sys.stdout.write("Content-type: text.html\r\n\r\n")
# sys.stdout.write("")
# sys.stdout.write("<html><body><p>")
# for row in rows:
#   sys.stdout.write("%s %s %s" % (row[0],row[1],row[2]))
#   sys.stdout.write("<br />")
# sys.stdout.write("</p></body></html>")