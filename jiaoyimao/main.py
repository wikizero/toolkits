# coding:utf-8
import os, sys

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5, id='Spider_jiaoyimao')
def run_spider():
	os.system('scrapy crawl world')
    print 'My spider is running, Now is %s' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 每隔5秒运行一次my_job1
# sched.add_job(run_spider, 'interval', minutes=3, id='Spider_jiaoyimao') # seconds


# 每隔5秒运行一次my_job2
# sched.add_job(my_job2,'cron',second='*/5',id='my_job2')

sched.start()
