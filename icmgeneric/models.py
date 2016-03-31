import datetime
from django.db import models

class HTMLImage(models.Model):
    upload = models.FileField(upload_to="uploads/htmlimages/%Y/%m/%d/")
    date_created = models.DateTimeField(default=datetime.datetime.now)
    is_image = models.BooleanField(default=True)