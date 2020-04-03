from celery import Celery

celery_app = Celery("meiduo")  # 传递一个名字,自己定义
# 导入配置文件
celery_app.config_from_object("celery_tasks.config")  # 格式:从开始执行文件的地方对应的目录开始导入对应的文件名,注释:入口文件manage.py
# 自动注册celery任务      传入一个列表,里面指明tasks.py文件所在的目录,就会自动找到对应的tasks.py文件
celery_app.autodiscover_tasks(['celery_tasks.test'])

# 补充:如果使用Django中内置的方法,会读取Django内置配置文件,这个时候需要加上下面的代码,读取配置文件,才能在celery中运行Django的程序(Django内置发送邮件)
# 为celery使用django配置文件进行设置(代码放在开头的地方即可)
import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'