from django.contrib.sitemaps import Sitemap
from .models import Page
from django.db.models import Q

__all__ = ['sitemaps']


class PageSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        exclude = []
        return Page.objects.filter(~Q(slug__in=exclude))

    def priority(self, obj):
        if obj.slug == 'home':
            return 1
        return 0.8

sitemaps = {
    'pages': PageSitemap,
}