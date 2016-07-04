# -*- coding: utf-8 -*-
import  urllib2,json,csv,sqlite3

class user_location(object):
    def __init__(self,ip,uid):
        self.ip = ip
        self.uid = uid
        self.num= num

    # 获取IP对应的GPS地址
    def get_mercator(self):
        url = 'http://api.map.baidu.com/location/ip?ak=fg493cr6UEjeaplnhuUNnc1zxFVxu7hV&ip=%s&coor=bd09ll'%(self.ip)
        req = urllib2.Request(url)

        resp = urllib2.urlopen(req)
        content = resp.read()
        jdata = json.loads(content)
        lista = ['0','0']
        if (jdata["status"] == 0 and len(jdata["content"]["point"]["x"]) != 0 and len(jdata["content"]["point"]["y"]) != 0):
            try:
                lista = [jdata["content"]["point"]["x"],jdata["content"]["point"]["y"]]
                print('****')
            except KeyError:
                print('no location')
        return lista

    # 将GPS地址导入数据表
    def trans_DB(self):
        conn = sqlite3.connect('E:\PycharmProjects\location.db')
        cursor = conn.cursor()
        listcsv = self.get_mercator()

        lat = listcsv[0]                                            #接收传入的经度
        yat = listcsv[1]                                            #接收传入的维度
        data = [self.num,self.ip,self.uid,lat,yat]
        try:
            cursor.execute("insert into test2 (num,IP,ID,x,y) values (?,?,?,?,?)",data)
        finally:
            # cursor.execute("select * from location")
            # values = cursor.fetchall()
            # print values
            conn.commit()
            cursor.close()
            conn.close()

def list2json(listdata):
    dictresult = {'lat':listdata[0],'lng':listdata[1]}
    jsonresult = json.dumps(dictresult)
    print jsonresult



with open('G:\data\khh_ip_02530521.csv',"r") as f1:
     num = 1
     rawfile = csv.reader(f1)
     huainan = user_location('n','dfff')
     for row in rawfile:
         huainan.ip = row[1]
         huainan.uid = row[0]
         huainan.num = num
         if huainan.ip == 'None':
            continue
         huainan.trans_DB()
         num = num + 1


