# -*- coding: utf-8 -*-
import urllib, urllib2,json,csv,sqlite3

conn = sqlite3.connect('E:\PycharmProjects\location.db')
cursor = conn.cursor()
cursor.execute("create table location_specific (num int primary key,id varchar(15),ip varchar,lat float,lng float,radius float)")








# get_mercator('36.33.13.191')
# with open("I:\sample.csv","r") as f1:
#     uId = csv.reader(f1)
#     for row in uId:
#         if row[0] != 'ID':
#             print(row[1])
#             listcsv = get_mercator(row[1])
#             cID = row[0]
#             lat = listcsv[0]
#             yat = listcsv[1]
#             data = [cID,lat,yat]
#             try:
#                 cursor.execute("insert into location (ID,x,y) values (?,?,?)",data)
#             finally:
#                 cursor.execute("select * from location")
#                 values = cursor.fetchall()
#                 print values
#
# value = cursor.execute('select * from location')
# print cursor.fetchall()
# cursor.close()
# conn.commit()
# conn.close()








