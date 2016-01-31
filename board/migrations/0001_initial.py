# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_auto_20160130_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('created_date', models.DateTimeField(auto_created=True)),
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('created_date', models.DateTimeField(auto_created=True)),
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=300)),
                ('board_id', models.ForeignKey(to='board.board')),
                ('double_comment_id', models.ForeignKey(to='board.comment')),
                ('user_id', models.ForeignKey(to='authen.hyu_users')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='category_id',
            field=models.ForeignKey(to='board.category'),
        ),
        migrations.AddField(
            model_name='board',
            name='user_id',
            field=models.ForeignKey(to='authen.hyu_users'),
        ),
    ]
