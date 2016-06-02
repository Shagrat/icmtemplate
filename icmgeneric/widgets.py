from django.contrib.admin.templatetags import admin_static
from django import forms


class RedactorWidgetBase(object):
    def _media(self):
        js = [
                "//code.jquery.com/jquery-latest.min.js",
                "//code.jquery.com/ui/1.11.1/jquery-ui.min.js",
                "admin/js-10/redactor.js",
                "admin/js-10/fontcolor.js",
                'admin/js-10/fontsize.js',
                'admin/js-10/imagemanager.js',
                'admin/js-10/video.js',
                'admin/js-10/table.js',
                'admin/js-10/fullscreen.js',
                "admin/js-10/redactor.init.js"
        ]
        js = [admin_static.static(path) for path in js]

        css = [
            "admin/css-10/redactor.css",
            "//code.jquery.com/ui/1.11.1/themes/smoothness/jquery-ui.css"
        ]
        css = {'all': [admin_static.static(path) for path in css]}

        return forms.Media(css=css, js=js)

    media = property(_media)


class RedactorWidget(forms.Textarea, RedactorWidgetBase):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'redactor'}
        if attrs:
            default_attrs.update(attrs)
        super(RedactorWidget, self).__init__(default_attrs)
