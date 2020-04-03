import datetime

from django.db.models import DateTimeField, Manager, Model,NullBooleanField,BooleanField


class BaseModelManager(Manager):
    '''模型管理类,可自定制常用的方法'''

    def filter(self, *args, **kwargs):
        '''
            filter定制:仅仅返回没有删除的内容
        '''
        return super().filter(is_deleted=False ,*args, **kwargs)

    def all(self):
        '''
            all定制:仅仅返回没有删除的内容
        '''
        return super().all().filter(is_deleted=False)


class BaseModel(Model):
    create_time = DateTimeField('创建日期', auto_now_add=True,null=True, blank=True)
    update_time = DateTimeField('修改时间', auto_now=True, null=True, blank=True)
    delete_time = DateTimeField('删除时间', null=True, blank=True)
    is_deleted = BooleanField(default=False)
    objects = BaseModelManager()

    def set_deleted(self):
        '''
            逻辑删除
        '''
        self.is_deleted = True
        self.delete_time = datetime.datetime.now()
        self.save()

    class Meta:
        abstract = True  # 说明是抽象模型类, 用于继承使用，数据库迁移时不会创建BaseModel的表



