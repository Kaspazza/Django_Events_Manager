# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-20 22:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20180520_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(blank='true', default=datetime.datetime(2018, 5, 20, 22, 36, 36, 764234)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2018, 5, 20)),
        ),
    ]