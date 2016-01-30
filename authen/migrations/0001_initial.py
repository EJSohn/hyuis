# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('admission_year', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('self_introduce', models.TextField(null=True)),
            ],
        ),
    ]
