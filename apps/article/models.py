from django.db import models

from exlib.sql_extension import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=10, help_text="类别")
    sub = models.ForeignKey('self', null=True, blank=True, related_name="category", verbose_name='父类别')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'


class Book(BaseModel):
    """书籍详情"""

    book_id = models.CharField(max_length=60, null=True, blank=True, help_text="源id")
    last_update = models.DateTimeField(null=True, blank=True, help_text="源最新更新时间")
    name = models.CharField(max_length=30, null=True, blank=True, help_text="名称")
    description = models.CharField(max_length=512, null=True, blank=True, help_text="简介")
    img = models.CharField(max_length=256, null=True, blank=True, help_text="封面")
    author = models.CharField(max_length=16, null=True, blank=True, help_text="作者")
    last_node = models.CharField(max_length=64, null=True, blank=True, help_text="最新章节名称")
    last_node_id = models.CharField(max_length=128, null=True, blank=True, help_text="最新章节id")
    state = models.SmallIntegerField(choices=((0, "连载"), (1, "完结")), help_text="状态")
    category = models.ForeignKey("Category", related_name="book", help_text="分类")
    score = models.FloatField(default=8.0, help_text="评分")
    first_node = models.CharField(max_length=64, null=True, blank=True, help_text="第一章")
    node_nums = models.IntegerField(default=0)
    level = models.SmallIntegerField(choices=((0, "免费"), (1, "福利书")), default=0)
    words = models.BigIntegerField(default=0, help_text="字数")
    columns = models.TextField(default='', help_text="章节列表(json)")
    charge_chapter = models.IntegerField(default=3, help_text="收费书籍开始付费章节")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '小说'


class Chapter(BaseModel):
    """章节详情"""
    name = models.CharField(max_length=64, null=False, blank=False, help_text="名称")
    book = models.ForeignKey("Book", related_name="chapter", help_text="书籍")
    words = models.IntegerField(default=0, help_text="字数")
    price = models.SmallIntegerField(default=0, help_text="价格")
    content = models.TextField(help_text="内容")

    class Meta:
        verbose_name = '章节'


class Comment(BaseModel):
    """评论"""
    user = models.ForeignKey("users.User", null=False, related_name="comment", help_text="评论人")
    nick = models.CharField(max_length=64, help_text="昵称")
    content = models.CharField(max_length=10, help_text="内容")
    book = models.ForeignKey(Book, related_name="comment", null=False, help_text="所属书")
    sub = models.ForeignKey('self', null=True, blank=True, related_name="comment", verbose_name='子评论')

    class Meta:
        verbose_name = '评论'


class Feedback(BaseModel):
    NORMAL, RECHARGE = 1, 2
    MSG_TYPE = ((NORMAL, '普通类型'), (RECHARGE, '充值类型'))

    user = models.ForeignKey('users.User')
    contact = models.CharField(max_length=255, default='null', help_text="联系方式")
    content = models.TextField(null=True, default=None, help_text="内容")
    version = models.CharField(max_length=64, null=True, help_text="设备版本")
    platform = models.CharField(max_length=128, default='android', null=True, help_text="系统平台")

    msg_type = models.SmallIntegerField(choices=MSG_TYPE, default=1, help_text="反馈类型")

    class Meta:
        verbose_name = '反馈'


class RedisReadHistory(BaseModel):
    user = models.ForeignKey('users.User')
    book = models.ForeignKey('Book')
    book_name = models.CharField(max_length=64, help_text="书名")
    chapter_id = models.IntegerField(help_text="当前章节")
    chapter_name = models.CharField(max_length=64, help_text="章节名")
    price = models.IntegerField(default=10, help_text="购买章节的价格")

    class Meta:
        verbose_name = '阅读历史'


class RedisBookStatistic(BaseModel):
    book = models.ForeignKey("Book")
    visit_num = models.BigIntegerField(default=0, help_text="访问量")
    pay_num = models.BigIntegerField(default=0, help_text="支付次数")
    collect_num = models.BigIntegerField(default=0, help_text="收藏次数")
    recommend_num = models.BigIntegerField(default=0, help_text="推荐次数")
    comment_num = models.IntegerField(default=0, help_text="评论数")

    class Meta:
        verbose_name = '统计'


class RedisBookShelf(Book):
    user = models.ForeignKey("users.User", null=False, related_name="shelf", help_text="评论人")

    class Meta:
        verbose_name = '书架'


class RedisRecommendBook(Book):

    class Meta:
        verbose_name = '推荐书'


class RedisBanner(Book):

    BOY, GIRL, FEATURED, WELFARE = 1, 2, 3, 4
    CHANNEL = ((BOY, '男频'), (GIRL, '女频'), (FEATURED, '精选'), (WELFARE, '福利'))

    TOP, DETAIL = 1, 2
    POSITION = ((TOP, '顶部'), (DETAIL, '详情内'))

    cover_pic = models.CharField(max_length=128, help_text="大封面图面地址")
    channel = models.SmallIntegerField(choices=CHANNEL, help_text="所属频道")
    position = models.SmallIntegerField(choices=POSITION, help_text="所在位置")

    class Meta:
        verbose_name = 'Banner栏'


class RedisHotWords(BaseModel):
    word = models.CharField(max_length=16, help_text="热词")

    class Meta:
        verbose_name = '热词搜索'



