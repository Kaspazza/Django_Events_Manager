# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-21 01:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20180520_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(blank='true', default=datetime.datetime(2018, 5, 21, 1, 19, 19, 299827)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2018, 5, 21)),
        ),
    ]