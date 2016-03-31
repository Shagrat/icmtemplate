from django import template

register = template.Library()

def inline(context, format_string):

    try:
        obj, field = (context[format_string.split('.')[0]], format_string.split('.')[1])
    except Exception, e:
        print e
        raise template.TemplateSyntaxError("Inline tag requires context object")
    path = '%s-%s-%s-%s' % (obj._meta.app_label, obj.__class__.__name__, obj.pk, field)
    return '<span id="%s" class="redactor" data-inline-path="%s">%s</span>' % (path, path, getattr(obj, field))

register.simple_tag(takes_context=True)(inline)