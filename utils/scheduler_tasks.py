import datetime

from apscheduler.events import JobSubmissionEvent, JobExecutionEvent
from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger


def aps_test():
    print("ok")



def my_listener(event):
    '''
        监听定时器任务监听机制
    '''
    if isinstance(event, JobSubmissionEvent):
        print("任务{}触发执行".format(event.job_id))
    if isinstance(event, JobExecutionEvent) and event.exception:
        print("任务{}抛出异常:{}".format(event.job_id, event.exception))

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///db.sqlite3')  #定时器任务持久化地址
}

scheduler = BlockingScheduler(jobstores=jobstores)

scheduler.add_job(func=aps_test,
                  trigger=CronTrigger(hour=20, minute=48),
                  replace_existing=True,
                  id="sb")

scheduler.add_job(func=aps_test,
                  replace_existing=True,
                  trigger=DateTrigger(run_date=datetime.datetime.now() + datetime.timedelta(seconds=12)),
                  id="sbsb")

scheduler.add_job(func=aps_test,    # 任务函数
                  trigger=IntervalTrigger(seconds=5),       # 执行计划
                  replace_existing=True,
                  id="sbsbsb"           # 唯一的
                  )

scheduler.add_listener(my_listener)
scheduler.start()
