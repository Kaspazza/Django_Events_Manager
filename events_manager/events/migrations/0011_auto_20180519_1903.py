# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-19 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20180519_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]