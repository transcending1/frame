from apps.users.models import User
from django.core.cache import cache #引入缓存模块
cache.set('key', 'value', 30*60)      #写入key为key，值为value的缓存，有效期30分钟
cache.has_key('key') #判断key为k是否存在
print(cache.get('key'))    #获取key为k的缓存