# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_auto_20160129_0806'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='hyu_users',
        ),
    ]
