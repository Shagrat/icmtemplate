from django.db import models
from icmgeneric.utils.orderable import OrderField
from django.utils.safestring import mark_safe
from orderable.models import Orderable


class GenericSiteElement(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class GenericSlider(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __unicode__(self):
       return self.name


class GenericSlide(Orderable):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider/', blank=True)
    caption = models.TextField(max_length=100, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('sort_order', )
        abstract = True

    def __unicode__(self):
        return self.name


class GenericPage(Orderable):
    title = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=100, db_index=True, unique=True, null=True,
                            help_text=mark_safe('(Do not change this field after creating a page.)'))
    meta_keywords = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_image = models.ImageField(upload_to='meta/og', null=True, blank=True)
    robots = models.CharField(max_length=255, blank=True)
    header = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ('sort_order',)
        abstract = True

    def __unicode__(self):
        return self.slug


class GenericNameContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title