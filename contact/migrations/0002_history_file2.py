# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='file2',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=b'tmp'),
        ),
    ]