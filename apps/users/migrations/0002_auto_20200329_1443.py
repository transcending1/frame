# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-29 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, help_text='手机号', max_length=11, null=True, verbose_name='手机号'),
        ),
    ]
