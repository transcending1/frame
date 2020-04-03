from django.db.models import CharField, DecimalField, DateTimeField, IntegerField, TextField, ForeignKey, \
    ManyToManyField,SmallIntegerField

from exlib.sql_extension import BaseModel
from django.db import models


class Blog(BaseModel):
    CATEGORY_CHOICES = (
        (0, '小说'),
        (1, '论文'),
        (2, '文章'),
        (3, '漫画'),
        (4, '内容'),
        (5, '微信'),
    )
    def __str__(self):
        return self.name

    class Meta:

        verbose_name = '博客'
        verbose_name_plural = verbose_name


    name = CharField(max_length=11,null=True, blank=True,verbose_name="书籍名称", help_text='书籍名称')
    price = DecimalField(max_digits=8,decimal_places=2,null=True, blank=True,verbose_name="书籍价格", help_text='书籍价格')
    category = SmallIntegerField(null=True, blank=True,choices=CATEGORY_CHOICES,verbose_name="书籍类型", help_text='书籍类型')
    comment = TextField(null=True, blank=True,verbose_name="经典书籍评论", help_text='经典书籍评论')

    @property
    def extra_name(self):
        return "test_{}".format(self.name)


class Article(BaseModel):
    name = CharField(max_length=11,blank=True)
    price = DecimalField(blank=True,max_digits=8,decimal_places=2)
    content = TextField(blank=True)
    blog = ForeignKey(Blog,related_name="article", on_delete=models.CASCADE)


class Fans(BaseModel):
    name = CharField(max_length=11,blank=True)
    price = DecimalField(blank=True,max_digits=8,decimal_places=2)
    content = TextField(blank=True)
    article = ManyToManyField(Article,related_name="fans")
