# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip=117.89.35.58'


req = urllib2.Request(url)

req.add_header("apikey","679b376c2f573415656b42277141b29d")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    s = content.decode("unicode-escape")
    print(s)