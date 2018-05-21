from __future__ import unicode_literals
import datetime
from django import forms
from django.db import models
from django.core.exceptions import ValidationError


class Event(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(default=datetime.date.today())
    duration = models.TextField(default='0', blank='true')
    created_at = models.DateTimeField(default=datetime.datetime.now(), blank='true')
    def save(self, *args, **kwargs):
        if self.date < str(datetime.date.today()):
            raise django.core.exceptions.ValidationError("The date cannot be in the past!")
        super(Event, self).save(*args, **kwargs)
