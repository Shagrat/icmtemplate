from django.db import models


class OrderField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['null'] = True
        kwargs['blank'] = True
        kwargs['editable'] = True
        super(OrderField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if not getattr(model_instance, self.attname) and not model_instance.pk:
            m = model_instance.__class__.objects.aggregate(o=models.Max(self.attname))['o'] or 0
            setattr(model_instance, self.attname, m + 1)
        return super(OrderField, self).pre_save(model_instance, add)
