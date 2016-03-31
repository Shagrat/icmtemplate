from __future__ import unicode_literals
import json
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from image_cropping import ImageRatioField
from icmgeneric.base import GenericSlide, GenericPage
from orderable.models import Orderable
from django.utils.timezone import now


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
