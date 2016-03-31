from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import SiteElement, Page, Testimonial, WhyUs
from icmgeneric.utils import simple
from portfolio.models import Gallery


def robots(request):
    data = SiteElement.objects.get(key='robots').value
    return HttpResponse(data, content_type='text/plain')


@simple('page.html')
def page(request, slug):
    _page = get_object_or_404(Page, slug=slug)

    return {
        'page': _page,
    }


@simple('index.html')
def home(request):
    _page = get_object_or_404(Page, slug='home')
    why_us = WhyUs.objects.filter(active=True)

    try:
        gallery = Gallery.objects.get(slug='portfolio')
    except Gallery.DoesNotExist:
        gallery = None
    photos = gallery.get_photos_on_home() if gallery else []

    return {
        'page': _page,
        'why_us': why_us,
        'photos': photos
    }
