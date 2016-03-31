from django.conf import settings
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import (
    Page, SiteElement
)
from icmgeneric.utils import RedactorFormMixin
from orderable.admin import OrderableAdmin, OrderableTabularInline


@admin.register(Page)
class PageAdmin(OrderableAdmin):
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'header', )
    list_display = ('title', 'slug')
    list_filter = []


    class AdminForm(forms.ModelForm, RedactorFormMixin):
        content = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'redactor'}),
            required=False
        )
        slug = forms.SlugField(max_length=100, help_text=mark_safe('(Do not change this field after creating a page.)'))

        class Meta:
            model = Page
            exclude = []

    form = AdminForm
    exclude = ['sort_order']


@admin.register(SiteElement)
class SiteElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'key')

    class SiteElementAdminForm(forms.ModelForm, RedactorFormMixin):
        def __init__(self, *args, **kwargs):
            super(SiteElementAdmin.SiteElementAdminForm, self).__init__(*args, **kwargs)
            if self.instance.is_wysiwyg:
                self.fields['value'].widget = forms.Textarea(attrs={'class': 'redactor'})
    if not settings.DEBUG:
        exclude = ('key', 'is_wysiwyg')

    def has_delete_permission(self, request, obj=None):
        if settings.DEBUG:
            return super(SiteElementAdmin, self).has_delete_permission(request, obj)
        return False

    def has_add_permission(self, request):
        if settings.DEBUG:
            return super(SiteElementAdmin, self).has_add_permission(request)
        return False

    form = SiteElementAdminForm