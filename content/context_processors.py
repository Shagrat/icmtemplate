import re
from django.contrib.sites.models import Site
from .models import SiteElement, Partner


def site_elements(request):
    d = {}
    for s in SiteElement.objects.all():
        n = re.sub(r'\W+', '_', s.key).lower()
        d[n] = s
    return {
        'se': d,
        'partners': Partner.objects.filter(active=True)
    }


def site(request):
    s = Site.objects.get_current()
    return {
        'site': s,
        'domain_with_schema': 'http://%s' % s,
        'url': 'http://%s%s' % (s, request.path),
    }