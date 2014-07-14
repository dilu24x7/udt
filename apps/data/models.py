from django.db import models
from apps.data.managers import EntryManager
from django.core.signals import request_finished
from apps.data import handlers

# Create your models here.

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    published = models.BooleanField(db_index=True,default=True)

    objects = EntryManager()

    def __unicode__(self):
        return "Title %s Created on %s"%(self.title,self.created)

request_finished.connect(handlers.request_finished)
