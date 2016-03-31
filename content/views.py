from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import SiteElement, Page
from icmgeneric.utils import simple


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
    return {
        'page': _page,
    }
