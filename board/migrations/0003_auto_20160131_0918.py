# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20160131_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category_id',
            field=models.ForeignKey(to='board.category'),
        ),
    ]
