import urllib2, requests, json, sys, urllib

def get_mercator(ip):
    # ip = '223.104.5.155'
    url = 'http://apis.baidu.com/rtbasia/ip_location/ip_location?ip=%s&v=1.1' % (ip)
    req = urllib2.Request(url)

    req.add_header("apikey", "fg493cr6UEjeaplnhuUNnc1zxFVxu7hV")

    resp = urllib2.urlopen(req)
    content = resp.read()
    if (content):
        print(content)


def run():
    f = open("I:\sample.txt")

    while 1:
        line = f.readline()
        get_mercator(line)
        if not line:
            break
    pass  # do something
    f.close()