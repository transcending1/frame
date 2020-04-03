import datetime

from bson import ObjectId
from mongoengine import Document as OriDocument, DateTimeField, BooleanField, queryset_manager, EmbeddedDocumentField, \
    ReferenceField, StringField
from mongoengine import fields


class MongoBaseModel(OriDocument):
    creator_id = StringField()
    updator_id = StringField()
    create_time = DateTimeField()
    update_time = DateTimeField()
    delete_time = DateTimeField()
    is_deleted = BooleanField(default=False)

    def set_deleted(self):
        '''
            逻辑删除
        '''
        self.is_deleted = True
        self.delete_time = datetime.datetime.now()
        self.save()

    @queryset_manager
    def ori_objects(doc_cls, queryset):
        return queryset

    @queryset_manager
    def objects(doc_cls, queryset):
        '''
            自定制querryset删选
        '''
        return queryset.filter(is_deleted=False)

    def update(self, **kwargs):
        self.update_time = datetime.datetime.now()
        super().update()

    def save(self, **kwargs):
        if not self.creator_id:
            from flask_login import current_user
            if current_user and not current_user.is_anonymous:
                self.creator_id = current_user.id
        if not self.create_time:
            if hasattr(self, 'created_time'):
                created_time = getattr(self, 'created_time')
                if type(created_time) is datetime.datetime:
                    self.create_time = created_time
            if not self.create_time:
                self.create_time = datetime.datetime.now()
        if self.pk and not self.updator_id:
            from flask_login import current_user
            if current_user and not current_user.is_anonymous:
                self.updator_id = current_user.id
        # todo 为了避免刷数据致使更新时间都大幅度延迟，目前暂时没有批量更新updata_time
        self.update_time = datetime.datetime.now()
        return super(MongoBaseModel, self).save(**kwargs)

    @classmethod
    def get_or_create(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except:
            return cls(**kwargs).save()

    def set_cached_property(self, k, v):
        """
            在行数据上存缓存。然后利用如下方式获取缓存数据。
            @cached_property
            def k(self):
                return v
        :param k:
        :param v:
        :return:
        """
        self.__dict__[k] = v

    def clear_cached_property(self, k):
        """
            清除对应的缓存数据
        :param k:
        :param v:
        :return:
        """
        if k in self.__dict__:
            del self.__dict__[k]

    @property
    def db_dict(self):
        return dict(self.to_mongo())

    @classmethod
    def create_with(cls, data_dict, ignore_fields=[]):
        s = cls()
        data_dict = {i: data_dict[i] for i in data_dict if i not in ignore_fields}
        MongoBaseModel.update_document(s, data_dict)
        return s

    def update_with(self, data_dict, ignore_fields=[]):
        """
            利用字典内容更新对象。屏蔽掉若干字段。
        :param data_dict:
        :param ignore_fields:
        :return:
        """
        data_dict = {i: data_dict[i] for i in data_dict if i not in ignore_fields}
        MongoBaseModel.update_document(self, data_dict)

    @staticmethod
    def update_document(document, data_dict):
        def field_value(field, value):
            if field.__class__ in (fields.ListField, fields.SortedListField):
                return [
                    field_value(field.field, item)
                    for item in value
                ]
            if field.__class__ in (
                    fields.ReferenceField,
            ) and type(value) in (ObjectId, str):
                return field.document_type.objects.get(pk=value)
            elif field.__class__ in (
                    fields.EmbeddedDocumentField,
                    fields.ReferenceField,
                    fields.GenericEmbeddedDocumentField,
                    fields.GenericReferenceField
            ):
                return field.document_type(**value)
            else:
                return value

        for key, value in data_dict.items():
            try:
                field = document._fields[key]
                if isinstance(field, (EmbeddedDocumentField, ReferenceField)) and value is None:
                    continue
                else:
                    setattr(
                        document, key,
                        field_value(field, value)
                    )
            except Exception as e:
                print('err field %s - value %s' % (key, str(value)))
                raise Exception('err field %s - value %s' % (key, str(value)))

    meta = {'abstract': True}
