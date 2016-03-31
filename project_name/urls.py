"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from content import views as content_views
from icmgeneric import views as icm_views
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from content.sitemaps import sitemaps as content_sitemaps
sitemaps = dict(content_sitemaps,)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax/filebrowser/$', icm_views.filebrowser),
    url(r'^ajax/fileupload/$', icm_views.upload_images),
    url(r'^ajax/imagelist/$', icm_views.recent_photos),
    url(r'^ajax/upload/$', icm_views.upload_images, name="upload_images"),
    url(r'^ajax/inline-save/$', icm_views.inline_save, name="inline_save"),
]

# Redirects
urlpatterns += [
]

urlpatterns += [
    # Errors
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),

    # Content
    url(r'^$', content_views.home, name='home'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^robots\.txt$', content_views.robots, name='robots'),

    # Page
    url(r'^(?P<slug>[\w\d\.-]+)/$', content_views.page, name='page'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
