import time
from ..main import celery_app  # 导入main.py 中的对象


@celery_app.task(name='send_sms_code')  # 加上装饰器:可以起一个名字
def send_sms_code(mobile):  # 自己定义一个函数,就是异步任务,可以传递参数,函数里面的一切都会交给
    time.sleep(5)
    print(mobile)
    return mobile