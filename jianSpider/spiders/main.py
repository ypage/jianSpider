# coding:utf8
import datetime
import time
import os

def doSth():
    os.system("scrapy crawl jianSp")

# 设置11:00开始执行爬虫爬取当天数据
def main(h=23, m=50):
    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            break
        time.sleep(60)
    doSth()


main()
