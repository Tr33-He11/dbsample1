# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

# url = 'http://apis.baidu.com/rtbasia/ip_location/ip_location?ip=%s&v=1.1'%('223.104.5.155')
#url = 'http://api.map.baidu.com/location/ip'
url = 'http://api.map.baidu.com/location/ip?ak=679b376c2f573415656b42277141b29d&ip=%s&coor=bd09ll'%('223.104.5.155')
req = urllib2.Request(url)

# req.add_header("apikey", "679b376c2f573415656b42277141b29d")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)

jdata = json.loads(content)
print(jdata)
