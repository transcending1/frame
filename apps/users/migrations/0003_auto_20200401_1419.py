# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-01 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200329_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='', help_text='头像', max_length=256, verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.SmallIntegerField(default=0, help_text='性别', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='nick',
            field=models.CharField(default='', help_text='昵称', max_length=64, verbose_name='nick'),
            preserve_default=False,
        ),
    ]
