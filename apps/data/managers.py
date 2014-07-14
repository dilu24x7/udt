# -*- coding: utf-8 *-*
from django.db import models

class EntryManager(models.Manager):

    def __init__(self):
        super(EntryManager, self).__init__()

    def published_entries(self):
        return self.model.objects.filter(published=True)
