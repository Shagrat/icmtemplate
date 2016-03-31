from django.apps import apps


def handle_form(form_name, request, form_class, pdf=None, pdf2=None, additional_context=None):
    Form = apps.get_model(app_label='contact', model_name='Form')
    return Form.objects.get(name=form_name).handle_form(request, form_class, pdf, pdf2, additional_context)


def is_blocked_ip(ip):
    BlacklistItem = apps.get_model(app_label='contact', model_name='Form')
    return not ip or BlacklistItem.objects.filter(ip=ip).count() == 0


def is_blocked(request):
    return is_blocked_ip(request.META.get('REMOTE_ADDR'))

