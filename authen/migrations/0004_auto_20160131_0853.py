# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_auto_20160130_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hyu_users',
            name='admission_year',
            field=models.IntegerField(),
        ),
    ]
