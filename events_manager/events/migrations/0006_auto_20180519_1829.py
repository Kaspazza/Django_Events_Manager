# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-19 18:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180519_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.PositiveIntegerField(blank='true', default='N/A', validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
