import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'd8pu%)38jj*7unflg%==ks$0hlwj7+0)t=yxz1@t-p!vs12a-8'
DEBUG = False
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'corsheaders',
    'rest_framework',
    'xadmin',  # xadmin
    'crispy_forms',  # xadmin
    'reversion',  # xadmin
    'apps.blog',
    'apps.users',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middleware.simple_middleware'
]

##################### redis服务器相关 #######################
# redis的版本不能过高 在2.10.6才能生效
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
##################### 用户鉴权相关 #############################
AUTH_USER_MODEL = 'users.User'
## 用redis来进行session的保存
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "session"

######################### DRF框架相关 #################################
REST_FRAMEWORK = {  # 添加, 后续的一切 RESTFUL配置都往里面添加
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),  # 过滤器
    'EXCEPTION_HANDLER': 'utils.exceptions.exception_handler.exception_handler',  # 全局异常捕获指定对应的函数进行异常捕获处理
    'DEFAULT_AUTHENTICATION_CLASSES': (  # JWT鉴权机制,Session鉴权机制等
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )
}

####################  JWT鉴权机制 + 用户认证机制 ########################
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # JWT生成的状态码的有效时间
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utils.authorizations_extension.jwt_response_payload_handler',  # 自定制用户登录成功后的返回信息
}
AUTHENTICATION_BACKENDS = [
    'utils.authorizations_extension.UsernameMobileAuthBackend',  # Django自定制认证机制:默认根据用户名和密码,可以进行拓展,变成自己想要的方式
]

######################## CORS跨域组件  ############################
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
CORS_ORIGIN_ALLOW_ALL = True  # 直接允许所有主机跨域

######################## url相关分配配置 #############################
ROOT_URLCONF = 'urls'  # 主url路径

########################## 数据库相关  ###################################
DATABASES = {  # sql
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

################## mongoengine连接 #################
from mongoengine import connect

connect('book', host='18.162.148.37', port=27017)  # mongoengine初始化

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

################################### 时间区间  ###############################################
LANGUAGE_CODE = 'zh-hans'  # 语言设置为 中文
TIME_ZONE = 'Asia/Shanghai'  # 时区设置为 亚洲/上海，注意没有北京
USE_I18N = True
USE_L10N = True
USE_TZ = True



###################模板相关#####################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


################# Django 静态文件收集地址 #################
STATIC_ROOT = os.path.join(BASE_DIR, 'static_file')   # 执行命令收集静态文件: python manage.py collectstatic

# 静态资源(调试的时候使用,部署的时候使用别的服务器来访问)
STATIC_URL = '/static/'  # 访问静态文件用到的url前缀(url以这种方式开头,那么Django不会去寻找动态资源了,直接到下面的文件寻找静态资源)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # 告知Django静态文件保存在哪个目录下(列表,可以多个地方存放静态资源)
# 前端访问示例: <img src="/static/imgs/avatar01.png" />



# 测试环境配置信息覆盖
try:
    from local_config import *

    IS_TEST = True
except:
    IS_TEST = False
