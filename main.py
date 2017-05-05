#!/usr/bin/env python
#encoding=utf-8
__author__ = 'Tim Liu'
__date__ = '2017/5/5 17:52'


import  urllib.request

import bs4
from bs4 import BeautifulSoup

import re
import codecs
import time
import os
import sqlite3

#获取html页面
def get_html(jobearea, keyword):
    url_temp = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea={jobarea}&keyword={keyword}&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    url = url_temp.format(jobarea=jobearea,keyword=urllib.request.quote(keyword))
    urlopen_content = urllib.request.urlopen(url)  # 打开网址
    html = urlopen_content.read().decode('gbk')   # 读取源代码并转为unicode
    return html

def parse_html_job_nums(html):
    soup = BeautifulSoup(html)
    # <div class="dw_table" id="resultList">
    # //*[@id="resultList"]/div[1]/div[3]
    #div1 = soup.find_all(id='resultList')

    # class 是python的关键字，记得加下划线,
    # 第3个div： <div class="rt">共3818条职位</div>
    div_childrens = soup.find_all("div", class_="dw_tlc")[0].children

    # div_childrens 是list_iterator 迭代器 类型
    job_nums = 0
    # 取出：<div class="rt">共7618条职位</div> 里面的数字：7618
    for child in div_childrens:
        # child有两种类型：<class 'bs4.element.Tag'> 与 <class 'bs4.element.NavigableString'>
        if isinstance(child, bs4.element.Tag):
            # 还有：['rt', 'order_time'] 、 ['rt', 'order_auto', 'dw_c_orange']、['chall']
            if child['class'] == ['rt']:
                # ['rt']有2个有，一个child.string等于“共7618条职位”，一个child.string为None
                if child.string:
                    # 用正则先去掉空格这些字符
                    compile_re = re.compile('\s*')
                    str = compile_re.sub('',child.string)
                    #print("======b===", str)
                    # 用正则取出数字
                    match_re = re.match(r".*?(\d+).*", str)
                    if match_re:
                        job_nums = int(match_re.group(1))
                    break

    print("job_nums=", job_nums)
    return job_nums


def save_sqlite(published_time,jobarea_name, job_nums, job_type ):
    """
        把爬取的数据写入sqlite数据库
    :param published_time: 职位爬取的时间
    :param jobarea_name:  职位的城市名称
    :param job_nums:      职位的个数
    :param job_type:     职位的类型：大数据 、 java、php、python、 android、iOS
    :return:
    """
    dbPath = '%s/jobs_analysis.db' % os.getcwd()
    print(dbPath)
    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    # 如果表不存在就新建表
    cur.execute('CREATE TABLE  IF NOT EXISTS  jobs_tb (id integer  NOT NULL  PRIMARY KEY AUTOINCREMENT DEFAULT 0,published_time Varchar(20) DEFAULT "",jobarea_name Varchar(20) DEFAULT "",job_nums int DEFAULT 0, job_type Varchar(20) DEFAULT "", job_mark Varchar(255) DEFAULT "" )')
    con.commit()

    # r 表示不转义，保留原始字符
    sqlStr = r'INSERT INTO jobs_tb (id,published_time, jobarea_name, job_nums, job_type) VALUES(NULL, "%s",  "%s", "%d", "%s")' % (published_time, jobarea_name, job_nums , job_type)
    print(sqlStr)
    cur.execute(sqlStr)
    con.commit()

    # 关闭数据库
    con.close()


def spider_jobs(job_type, jobarea_codes=[], jobarea_names=[]):
    file = codecs.open("jobs.txt", "a", "utf-8")
    file.write("================= " + job_type + " =================\n")
    for j in range(len(jobarea_codes)):
        # 日期时间
        time_str = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
        # 工作地名
        jobarea_name = jobarea_names[j]

        html = get_html(jobarea_codes[j], job_type)
        # 工作的职位数
        job_nums = parse_html_job_nums(html)

        # 数据保存到sqlite数据库
        save_sqlite(time_str, jobarea_name, job_nums, job_type)
        # 数据保存到txt文本文件中
        file.write(u"{0}\t{1}\t{2} \n".format(time_str, jobarea_name , job_nums ))

    #file.write(u"-----------------------------------\n")
    file.close()



if __name__ == '__main__':
    # 北京 ： jobarea=010000，
    jobarea_codes  = ["010000", "020000", "040000", "030200"]
    jobarea_names = [u"北京", u"上海", u"深圳", u"广州"]
    keywords = [u"大数据","java","Android", "iOS", "python", "php", "golang"]

    for i in range(len(keywords)):
        spider_jobs(keywords[i], jobarea_codes, jobarea_names)







