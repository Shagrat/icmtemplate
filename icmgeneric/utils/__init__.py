from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response


def simple(template):
    def d1(func):
        def d2(request, *args, **kwargs):
            r = func(request, *args, **kwargs)
            if isinstance(r, HttpResponse):
                return r
            else:
                return render_to_response(template, r, context_instance=RequestContext(request))
        return d2
    return d1


class RedactorFormMixin(object):
    class Media:
        css = {
            "all": ("admin/css-10/redactor.css", "//code.jquery.com/ui/1.11.1/themes/smoothness/jquery-ui.css")
        }
        js = (
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
        )

