#!/usr/bin/env python
#encoding=utf-8
__author__ = 'Tim Liu'
__date__ = '2017/6/17 13:50'

import random
import urllib
import time
from urllib.request import Request, urlopen

# 刷票 : 第三届中国外语微课大赛
def auto_vote(url_temp):

    random_decimal = random.random()
    url = url_temp.format(random=random_decimal)
    print(url);
    headers_list = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36",

    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
    "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)",
    "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)"]

    i = random.randint(0, len(headers_list) -1)
    print("headers_lis.len=", len(headers_list))
    print("i=", i)
    headers = { 'User-Agent' : headers_list[i] }
    sleeptimes = random.uniform(1, 10)
    print("sleeptimes=", sleeptimes)
    time.sleep(sleeptimes)
    req = urllib.request.Request(url, None, headers)
    try:
        # urllib2.urlopen("http://example.com", timeout = 1)
        urlopen_content = urlopen(req, timeout=30)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))

    html = urlopen_content.read().decode('gbk')   # 读取源代码并转为gbk
    print("html=", html)
    urlopen_content.close()

# http://weike.cflo.com.cn/play.asp?vodid=174906&e=5&from=groupmessage
if __name__ == '__main__':
    vote_nums = 9

    for i in range(0,vote_nums):
        # 欢迎您投票支持
        auto_vote( "http://weike.cflo.com.cn/js_support.asp?vodid=174906_5&xiangmu=5&nxxx={random}")
        # 已采用
        auto_vote( "http://weike.cflo.com.cn/js_useradopt.asp?vodid=174906&xiangmu=5&nzz={random}")
    print("总共刷票成功数：", vote_nums)



