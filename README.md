# python_spider_jobs
已经在python3.4、python3.5、python3.6测试通过 ， 技术栈：urllib+BeautifulSoup4+SQLite，用到的py库：beautifulsoup4、configparser，以后增加图表显示的功能   
python写的爬虫，爬取51job前程无忧、智联招聘的大城市（北京、上海、深圳、广州、杭州）各种编程语言职位的总条数。  
目前的岗位有：人工智能, 大数据, java, 前端, Android, iOS, python, php, go语言。  
爬取后分别保存到sqlite数据库与txt文本文件中。sqlite数据库一天只保存一次。但jobs.txt一天可以写入多次爬取的记录。    
