# -*- coding: utf-8 -*-
import  urllib2,json,csv

class user_location(object):
    def __init__(self,ip,uid):
        self.ip = ip
        self.uid = uid
 #       self.num= num

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

    #格式转换为json
    # def list2json(listdata):
    #     dictresult = {'lat':listdata[1],'lng':listdata[0]}
    #     jsonresult = json.dumps(dictresult)
    #     print jsonresult
    #     return jsonresult

    #导出json文件到txt
    def json2txt(self):
        listC = self.get_mercator()                             #获取地址list
        dictC = {}                                              #初始化字典
        if listC != ['0','0']:
            dictC = {'lng':listC[1] ,'lat':listC[0] }           #地址传如字典
            jsonD = json.dumps(dictC)                           #字典转为json
            file = open('g:\dict33.txt','a')                    #写入txt文本
            file.write(jsonD + ',')
            # print jsonD

    #生成没有重复元素的list串
    # def createList(self):
        # listD = []
        # if self.get_mercator() not in listD:
        #     listD.append(self.get_mercator())
        # return  listD





with open('G:\data\khh_ip_00330521.csv',"r") as f1:
     listD = []
     num = 0
     rawfile = csv.reader(f1)
     huainan = user_location('n','dfff')
     for row in rawfile:
         huainan.ip = row[1]
         huainan.uid = row[0]
         if huainan.ip == 'None':
             continue
         huainan.json2txt()
         if huainan.get_mercator() not in listD:
             listD.append(huainan.get_mercator())
         num = num + 1
     print num
     print len(listD)
