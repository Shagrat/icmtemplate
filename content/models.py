from __future__ import unicode_literals
from django.db import models
from icmgeneric.base import GenericPage


class SiteElement(models.Model):
    name = models.CharField(max_length=255, blank=True)
    key = models.CharField(max_length=255, unique=True)
    is_wysiwyg = models.BooleanField(default=False)
    value = models.TextField(blank=True)
    document = models.FileField(blank=True)

    def __unicode__(self):
        return '{name} ({key})'.format(name=self.name, key=self.key)

    class Meta:
        verbose_name = 'Site Element'
        verbose_name_plural = 'Site Elements'


class Page(GenericPage):
    pass
