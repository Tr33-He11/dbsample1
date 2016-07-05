# -*- coding: utf-8 -*-
import urllib2 , json


# 读取txt
# filesp = open('I:\sample.txt')
# try:
#     contant = filesp.read()
#     print(contant)
# finally:
#     filesp.close()


ip = '117.57.210.198'
# url = 'http://apis.baidu.com/rtbasia/ip_location/ip_location?ip=%s&v=1.1' % (ip)
# url = 'http://apis.baidu.com/rtbasia/ip_maxcoverage/ip_maxcoverage?ip=%s&amp;v=1.1'%(ip)
url = 'http://api.rtbasia.com/coor/get_maxcoverage?ip=%s&key=679b376c2f573415656b42277141b29d' % (ip)
req = urllib2.Request(url)

# req.add_header("key", "679b376c2f573415656b42277141b29d")
resp = urllib2.urlopen(req)
content = resp.read()
# jdata = json.loads(content)
# lista = ['0','0']
# if (jdata["status"] == 0 and len(jdata["content"]["point"]["x"]) != 0 and len(jdata["content"]["point"]["y"]) != 0):
#     lista = [jdata["content"]["point"]["x"],jdata["content"]["point"]["y"]]
#     print lista
print content



#def run():
 #   f = open("I:\sample.txt")
#
 #   while 1:
  #      line = f.readline()
   #     get_mercator(line)
    #    if not line:
     #       break
   # pass  # do something
   # f.close()



