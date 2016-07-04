# -*- coding: utf-8 -*-
import urllib, urllib2,json,csv,sqlite3


conn = sqlite3.connect('E:\PycharmProjects\location.db')
cursor = conn.cursor()
# cursor.execute("insert into location (ID,x,y) values ('TD', 'edsss', 'ddddd')")
# cursor.execute("delete from ItL where uID = 'abcc'")
# cursor.execute("create table locat (id varchar(30) primary key,x float ,y float)")

# #根据传入的IP获得GPS
def get_mercator(ip):
    url = 'http://api.map.baidu.com/location/ip?ak=fg493cr6UEjeaplnhuUNnc1zxFVxu7hV&ip=%s&coor=bd09ll'%(ip)
    req = urllib2.Request(url)

    resp = urllib2.urlopen(req)
    content = resp.read()
    jdata = json.loads(content)
    lista = []

    try:
        lista = [jdata["content"]["point"]["x"],jdata["content"]["point"]["y"]]
        print('****')
    except KeyError:
        print('no location')

    return lista

with open("I:\sample.csv","r") as f1:
    uId = csv.reader(f1)
    for row in uId:
        if row[0] != 'ID':
            print(row[1])
            listcsv = get_mercator(row[1])
            cID = row[0]
            lat = listcsv[0]
            yat = listcsv[1]
            data = [cID,lat,yat]
            try:
                cursor.execute("insert into location (ID,x,y) values (?,?,?)",data)
            finally:
                cursor.execute("select * from location")
                values = cursor.fetchall()
                print values

value = cursor.execute('select * from location')
print cursor.fetchall()
cursor.close()
conn.commit()
conn.close()