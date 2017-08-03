# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 14:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 8, 3, 14, 43, 33, 677886, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
