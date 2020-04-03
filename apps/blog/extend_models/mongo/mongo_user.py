from mongoengine import StringField

from exlib.mongo_extension import MongoBaseModel


class User(MongoBaseModel):
    name = StringField()
    meta = {'collection': 'book'}