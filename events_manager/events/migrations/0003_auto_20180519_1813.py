# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-19 18:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
