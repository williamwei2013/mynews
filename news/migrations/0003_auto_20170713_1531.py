# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170713_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='likes11111',
            new_name='likes',
        ),
    ]
