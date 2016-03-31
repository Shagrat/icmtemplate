from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    url(r'^ajax/filebrowser/$', views.filebrowser),
    url(r'^ajax/fileupload/$', views.upload_images),
    url(r'^ajax/imagelist/$', views.recent_photos),
    url(r"^ajax/upload/$", views.upload_images, name="upload_images")
]
