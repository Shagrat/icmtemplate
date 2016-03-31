from django.template.loader import render_to_string
from inplaceeditform.commons import get_static_url
from inplaceeditform.fields import BaseAdaptorField


class RedactorAdaptor(BaseAdaptorField):

    @property
    def name(self):
        return 'Redactor adaptor'

    def render_value_edit(self):
        value = self.render_value()
        return render_to_string('redactor/inline.html',
                                {'value': value,
                                 'adaptor': self,
                                 'field': self.get_field()})
    def render_media_field(self,
                           template_name="redactor/inline_media.html",
                           extra_context=None):
        extra_context = extra_context or {}
        context = {'STATIC_URL': get_static_url()}
        context.update(extra_context)
        return super(RedactorAdaptor, self).render_media_field(template_name=template_name,
                                                                   extra_context=context)