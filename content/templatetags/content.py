from django import template
from django.contrib.sites.models import Site
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def render_blocks(context, page):
    return mark_safe(page.get_rendered_blocks_str(context))


@register.filter
def get_url(path):
    site = Site.objects.get_current()
    if path:
        return 'http://%(domain)s%(path)s' % {'domain': site.domain, 'path': path}
    return ''


@register.inclusion_tag('tags/dummy.html', takes_context=True)
def pagination(context, page, begin_pages=1, end_pages=1,
                      before_pages=2, after_pages=2,
                      template='tags/pagination.html'):
    """
    Return a Digg-like pagination,
    by splitting long list of page into 3 blocks of pages.
    """
    GET_string = ''
    for key, value in context['request'].GET.items():
        if key != 'page':
            GET_string += '&%s=%s' % (key, value)
    
    page_range = list(page.paginator.page_range)
    begin = page_range[:begin_pages]
    end = page_range[-end_pages:]
    middle = page_range[max(page.number - before_pages - 1, 0):
                        page.number + after_pages]
        
    if set(begin) & set(middle):  # [1, 2, 3], [2, 3, 4], [...]
        begin = sorted(set(begin + middle))  # [1, 2, 3, 4]
        middle = []
    elif begin[-1] + 1 == middle[0]:  # [1, 2, 3], [4, 5, 6], [...]
        begin += middle  # [1, 2, 3, 4, 5, 6]
        middle = []
    elif middle[-1] + 1 == end[0]:  # [...], [15, 16, 17], [18, 19, 20]
        end = middle + end  # [15, 16, 17, 18, 19, 20]
        middle = []
    elif set(middle) & set(end):  # [...], [17, 18, 19], [18, 19, 20]
        end = sorted(set(middle + end))  # [17, 18, 19, 20]
        middle = []
        
    if set(begin) & set(end):  # [1, 2, 3], [...], [2, 3, 4]
        begin = sorted(set(begin + end))  # [1, 2, 3, 4]
        middle, end = [], []
    elif begin[-1] + 1 == end[0]:  # [1, 2, 3], [...], [4, 5, 6]
        begin += end  # [1, 2, 3, 4, 5, 6]
        middle, end = [], []

    return {'template': template,
            'page': page,
            'begin': begin,
            'middle': middle,
            'end': end,
            'GET_string': GET_string}

