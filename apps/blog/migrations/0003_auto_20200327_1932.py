# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-27 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200327_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.SmallIntegerField(blank=True, choices=[(0, '小说'), (1, '论文'), (2, '文章'), (3, '漫画'), (4, '内容'), (5, '微信')], null=True),
        ),
    ]
