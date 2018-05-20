from __future__ import unicode_literals
from datetime import datetime
from django import forms
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(default=datetime.now)
    duration = models.TextField(default='0', blank='true')
    created_at = models.DateTimeField(default=datetime.now, blank='true')

    def __str__(self):
        return self.title
