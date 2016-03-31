from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
import re


class BaseForm(forms.Form):
    def _clean_phone(self, name):
        phone = self.cleaned_data[name]
        if phone and not re.match(r'(^[\d\s\(\)\+-]+$)', phone):
            raise forms.ValidationError("Valid characters 0-9, (, ), +, whitespace")
        return phone

    def clean_phone(self):
        return self._clean_phone('phone')


class ContactForm(BaseForm):
    name = forms.CharField(label='Name*', widget=forms.TextInput(attrs={}))
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={}), required=False)
    email = forms.EmailField(label='Email*', widget=forms.EmailInput(attrs={}))
    message = forms.CharField(
        label='Comments*',
        widget=forms.Textarea(attrs={}),
    )
    # captcha = ReCaptchaField(widget=ReCaptchaWidget())