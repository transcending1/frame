# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-02 05:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('is_deleted', models.BooleanField(default=False)),
                ('nick', models.CharField(help_text='昵称', max_length=64)),
                ('content', models.CharField(help_text='内容', max_length=10)),
            ],
            options={
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('is_deleted', models.BooleanField(default=False)),
                ('contact', models.CharField(default='null', help_text='联系方式', max_length=255)),
                ('content', models.TextField(default=None, help_text='内容', null=True)),
                ('version', models.CharField(help_text='设备版本', max_length=64, null=True)),
                ('platform', models.CharField(default='android', help_text='系统平台', max_length=128, null=True)),
                ('msg_type', models.SmallIntegerField(choices=[(1, '普通类型'), (2, '充值类型')], default=1, help_text='反馈类型')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '反馈',
            },
        ),
        migrations.CreateModel(
            name='RedisBanner',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='article.Book')),
                ('cover_pic', models.CharField(help_text='大封面图面地址', max_length=128)),
                ('channel', models.SmallIntegerField(choices=[(1, '男频'), (2, '女频'), (3, '精选'), (4, '福利')], help_text='所属频道')),
                ('position', models.SmallIntegerField(choices=[(1, '顶部'), (2, '详情内')], help_text='所在位置')),
            ],
            options={
                'verbose_name': 'Banner栏',
            },
            bases=('article.book',),
        ),
        migrations.CreateModel(
            name='RedisBookShelf',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='article.Book')),
                ('user', models.ForeignKey(help_text='评论人', on_delete=django.db.models.deletion.CASCADE, related_name='shelf', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '书架',
            },
            bases=('article.book',),
        ),
        migrations.CreateModel(
            name='RedisBookStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('is_deleted', models.BooleanField(default=False)),
                ('visit_num', models.BigIntegerField(default=0, help_text='访问量')),
                ('pay_num', models.BigIntegerField(default=0, help_text='支付次数')),
                ('collect_num', models.BigIntegerField(default=0, help_text='收藏次数')),
                ('recommend_num', models.BigIntegerField(default=0, help_text='推荐次数')),
                ('comment_num', models.IntegerField(default=0, help_text='评论数')),
            ],
            options={
                'verbose_name': '统计',
            },
        ),
        migrations.CreateModel(
            name='RedisHotWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('is_deleted', models.BooleanField(default=False)),
                ('word', models.CharField(help_text='热词', max_length=16)),
            ],
            options={
                'verbose_name': '热词搜索',
            },
        ),
        migrations.CreateModel(
            name='RedisReadHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('is_deleted', models.BooleanField(default=False)),
                ('book_name', models.CharField(help_text='书名', max_length=64)),
                ('chapter_id', models.IntegerField(help_text='当前章节')),
                ('chapter_name', models.CharField(help_text='章节名', max_length=64)),
                ('price', models.IntegerField(default=10, help_text='购买章节的价格')),
            ],
            options={
                'verbose_name': '阅读历史',
            },
        ),
        migrations.CreateModel(
            name='RedisRecommendBook',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='article.Book')),
            ],
            options={
                'verbose_name': '推荐书',
            },
            bases=('article.book',),
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '小说'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类'},
        ),
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name': '章节'},
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='sort_level',
        ),
        migrations.AddField(
            model_name='book',
            name='charge_chapter',
            field=models.IntegerField(default=3, help_text='收费书籍开始付费章节'),
        ),
        migrations.AddField(
            model_name='book',
            name='columns',
            field=models.TextField(default='', help_text='章节列表(json)'),
        ),
        migrations.AddField(
            model_name='book',
            name='score',
            field=models.FloatField(default=8.0, help_text='评分'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='price',
            field=models.SmallIntegerField(default=0, help_text='价格'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(help_text='分类', on_delete=django.db.models.deletion.CASCADE, related_name='book', to='article.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='article.Category', verbose_name='父类别'),
        ),
        migrations.AddField(
            model_name='redisreadhistory',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Book'),
        ),
        migrations.AddField(
            model_name='redisreadhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='redisbookstatistic',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Book'),
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(help_text='所属书', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='article.Book'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='article.Comment', verbose_name='子评论'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(help_text='评论人', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
