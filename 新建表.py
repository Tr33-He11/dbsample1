# -*- coding: utf-8 -*-
import urllib, urllib2,json,csv,sqlite3


conn = sqlite3.connect('E:\PycharmProjects\location.db')
cursor = conn.cursor()
# cursor.execute("insert into location (ID,x,y) values ('TD', 'edsss', 'ddddd')")
#  cursor.execute("delete from ItL where uID = 'abcc'")
cursor.execute("create table test2 (num integer primary key,IP varchar(30) ,ID varchar(16),x float ,y float)")