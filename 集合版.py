# -*- coding: utf-8 -*-
import  urllib2,json,csv,sqlite3

class user_location(object):

    listD = []

    def __init__(self,ip,uid):
        self.ip = ip
        self.uid = uid



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

    def remove(self):                                              #去除重复地址
        self.listD = self.get_mercator()
        if self.get_mercator() not in self.listD:
            self.listD.append(self.get_mercator())
        return self.listD



class location2DB(user_location):                                  #获取IP对应的GPS地址

    def list2DB(self):
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



class location2json(user_location):

    def list2json(self):
        listdata = []
        listdata = self.get_mercator()
        dictresult = {'lat':listdata[0],'lng':listdata[1]}
        jsonresult = json.dumps(dictresult)
        file = open('g:\dict20.txt','a')                    #写入txt文本
        file.write(jsonresult + ',')
        print jsonresult


     #导出json文件到txt
    # def json2txt(self):
    #     listC = self.get_mercator()                             #获取地址list
    #     dictC = {}                                              #初始化字典
    #     if listC != ['0','0']:
    #         dictC = {'lng':listC[1] ,'lat':listC[0] }           #地址传如字典
    #         jsonD = json.dumps(dictC)                           #字典转为json
    #         file = open('g:\dict33.txt','a')                    #写入txt文本
    #         file.write(jsonD + ',')
    #         # print jsonD




# with open('G:\data\khh_ip_00200521pp.csv',"r") as f1:
with open('I:\sample.csv','r') as f1:

     num = 0
     rawfile = csv.reader(f1)
     hefei = location2json('n','dfff')
     for row in rawfile:
         hefei.ip = row[1]
         hefei.uid = row[0]
         if hefei.ip == 'None' and num > 10:
            continue
         hefei.list2json()
         num = num + 1
         print num