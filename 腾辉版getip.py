# -*- coding: utf-8 -*-

import  urllib2,json,csv,sqlite3

class user_location(object):

    listD = []

    def __init__(self,ip,uid,num):
        self.ip = ip
        self.uid = uid
        self.num = num


    def get_wgs(self):

        # url = 'http://apis.baidu.com/rtbasia/ip_maxcoverage/ip_maxcoverage?ip=%s&amp;v=1.1'%(self.ip)
        url = 'http://api.rtbasia.com/coor/get_maxcoverage?ip=%s&key=679b376c2f573415656b42277141b29d' % (self.ip)
        req = urllib2.Request(url)

        # req.add_header("apikey","679b376c2f573415656b42277141b29d")

        resp = urllib2.urlopen(req)
        content = resp.read()
        jdata = json.loads(content)
        lista = ['0','0','0']
        # if jdata[0]["location"]["latitude"] != "None" or jdata[0]["location"]["longitude"] != "None":
        if len(jdata[0]) != 1:
            try:
                lista = [jdata[0]["location"]["latitude"],jdata[0]["location"]["longitude"],jdata[0]["location"]["radius"]]
                print lista
                return lista
            except KeyError:
                print('no location')

        else:
            return ['0','0','0']


    # def remove(self):                                              #去除重复地址
    #     self.listD = self.get_mercator()
    #     if self.get_mercator() not in self.listD:
    #         self.listD.append(self.get_mercator())
    #     return self.listD

    def WGS2BD09(self):                                             #将获取的WGS地址信息转为BD09百度坐标
        list = []
        listD = self.get_wgs()
        if listD == ['0','0','0']:
           list = [self.num,self.uid,self.ip,'0','0','0']           #获取WGS版的X,Y,radius
           return list
        else:
            locate = "%s,%s"%(listD[1],listD[0])
        # locate = "117.26251,31.852298"1
            url = "http://api.map.baidu.com/geoconv/v1/?coords=%s&from=1&to=5&ak=fg493cr6UEjeaplnhuUNnc1zxFVxu7hV"%(locate)    #老key
            req = urllib2.Request(url)
            resq = urllib2.urlopen(req)
            content = resq.read()
            BDcontent = json.loads(content)
            if BDcontent["status"] == 0:
                list = [BDcontent["result"][0]["x"],BDcontent["result"][0]["y"],listD[2]]
                return  list
            else:
                return ['0','0','0']

class location2json(user_location):

#     def list2json(self):
#         listdata = []
#         listdata = self.get_mercator()
#         dictresult = {'lat':listdata[0],'lng':listdata[1]}
#         jsonresult = json.dumps(dictresult)
#         file = open('g:\dict20.txt','a')                    #写入txt文本
#         file.write(jsonresult + ',')
#         print jsonresult


     # 导出json文件到txt
    def DB092txt(self):
        listC = self.WGS2BD09()                                 #获取地址list
        dictC = {}                                              #初始化字典
        if listC != ['0','0']:
            dictC = {'lng':listC[1] ,'lat':listC[0] }           #地址传如字典
            jsonD = json.dumps(dictC)                           #字典转为json
            print jsonD
            file = open('g:\dictTHreverse2.txt','a')            #写入txt文本
            file.write(jsonD + ',')

            # print jsonD

class location2sqlite(user_location):                                  #获取IP对应的GPS地址到数据库


    def list2sqlite(self):                                             #发送到数据库

        conn = sqlite3.connect('E:\PycharmProjects\location.db')
        cursor = conn.cursor()
        listcsv = self.WGS2BD09()

        lat = listcsv[0]                                            #接收传入的经度
        yat = listcsv[1]                                            #接收传入的维度
        radius = listcsv[2]
        data = [self.num,self.uid,self.ip,lat,yat,radius]
        try:
            cursor.execute("insert into ip2location3306 (num,id,ip,lat,lng,radius) values (?,?,?,?,?,?)",data)
        finally:
            # cursor.execute("select * from location")
            # values = cursor.fetchall()
            # print values
            conn.commit()
            cursor.close()
            conn.close()



# with open('G:\data\khh_ip_00200521pp.csv',"r") as f1:
with open('E:\PycharmProjects\dbsample1\data\khh_ip_0033.201606.csv','r') as f1:
     num = 1
     rawfile = csv.reader(f1)
     hefei = location2sqlite('n','dfff',0)
     for row in rawfile:
         hefei.ip = row[1]
         hefei.uid = row[0]

         if hefei.ip == 'None' or num > 500:
            continue
         hefei.list2sqlite()
         num = num + 1
         hefei.num = num

         print num

# url = 'http://apis.baidu.com/rtbasia/ip_location/ip_location?ip=99.90.64.33&amp;v=1.1'
# url = 'http://apis.baidu.com/rtbasia/ip_maxcoverage/ip_maxcoverage?ip=%s&amp;v=1.1'&(self.ip)
#
# req = urllib2.Request(url)
#
# req.add_header("apikey","679b376c2f573415656b42277141b29d")
#
# resp = urllib2.urlopen(req)
# content = resp.read()
# if(content):
#     print(content)


#
#
#