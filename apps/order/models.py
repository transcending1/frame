from django.db import models
from exlib.sql_extension import BaseModel


class NodeBuyRecord(BaseModel):
    """章节购买记录"""
    user = models.ForeignKey('User')
    book = models.ForeignKey('Book')
    book_name = models.CharField(max_length=64, help_text="书名")
    chapter = models.ForeignKey('Chapter')
    chapter_name = models.CharField(max_length=64, help_text="章节名")
    price = models.IntegerField(default=10,help_text="购买章节的价格")


class RechargeRecord(BaseModel):
    """充值记录"""

    FAILED, SUCCESS = 0, 1
    STATUS = ((FAILED, "失败"), (SUCCESS, "成功"))

    user = models.ForeignKey('User')
    money = models.IntegerField(default=0,help_text="充值金额，元'")
    coins = models.IntegerField(default=0,help_text="操作后书币")
    status = models.SmallIntegerField(choices=STATUS, help_text="充值结果")
    order_num = models.CharField(max_length=128, default='', help_text="订单号")


class Combo(BaseModel):
    Combo = {
        0: {'price': 38, 'coins': 3800 + 200},
        1: {'price': 58, 'coins': 5800 + 3000},
        2: {'price': 88, 'coins': 10000 + 10000}
    }
    price = models.SmallIntegerField(help_text="套餐价格")
    coins = models.IntegerField(help_text="充值书币")
    extra_coins = models.IntegerField(help_text="额外赠送书币")

