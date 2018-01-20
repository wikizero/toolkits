# coding:utf-8
import os, sys

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=3, id='Spider_world')
def run_spider():
    #info = '\nMy spider is running, Now is %s \n' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #with open('schedule.out', 'a+') as fp:
    #        fp.write(info)
    os.system('scrapy crawl world')


#@sched.scheduled_job('interval', minutes=1, id='database_backup')
#def db_backup():
#    info = '\nDatabase_backup is running, Now is %s \n' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#    with open('schedule.out', 'a+') as fp:
#        fp.write(info)    
#    os.comand('mysqldump -uroot -proot world info > ../info.sql')
# 每隔5秒运行一次my_job1
# sched.add_job(run_spider, 'interval', minutes=3, id='Spider_jiaoyimao') # seconds


# 每隔5秒运行一次my_job2
# sched.add_job(my_job2,'cron',second='*/5',id='my_job2')
#@sched.scheduled_job('interval', minutes=30, id='Spider_sword')
#def run_spider():
    #info = '\nMy spider is running, Now is %s \n' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #with open('schedule.out', 'a+') as fp:
    #        fp.write(info)
#    os.system('scrapy crawl sword')


sched.start()
