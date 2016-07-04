# -*- coding: utf-8 -*-
import urllib2,json

# def WGS2BD09(wgslocate):

# locate = wgslocate
locate = "117.26251,31.852298"
url = "http://api.map.baidu.com/geoconv/v1/?coords=%s&from=1&to=5&ak=fg493cr6UEjeaplnhuUNnc1zxFVxu7hV"%(locate)    #老key
req = urllib2.Request(url)

resq = urllib2.urlopen(req)

content = resq.read()
# print  content

BDcontent = json.loads(content)
# locate = "%s,%s"%(self.get_wgs()[0],self.get_wgs()[1])
locate1 = "%s,%s"%(BDcontent["result"][0]["x"],BDcontent["result"][0]["y"])
print  content
# print(BDcontent["result"][0]["x"],BDcontent["result"][0]["y"])





# 117.27450535265,"y":31.856327032295
# 117.26251,31.852298
