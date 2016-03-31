import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from icmgeneric.utils import simple
from models import HTMLImage
# from django.db.models.loading import get_model
from django.apps import apps


def filebrowser(request):
    text = render_to_string('redactor/filebrowser.html', {})
    return HttpResponse(text, content_type="text/plain")


@csrf_exempt
@require_POST
@login_required
def upload_images(request):
    images = []
    for f in request.FILES.getlist("file"):
        obj = HTMLImage.objects.create(upload=f, is_image=True)
        images.append({"filelink": obj.upload.url})
    return HttpResponse(json.dumps(images), content_type="application/json")


@login_required
def recent_photos(request):
    images = [
        {"thumb": obj.upload.url, "image": obj.upload.url}
        for obj in HTMLImage.objects.filter(is_image=True).order_by("-date_created")[:20]
    ]
    return HttpResponse(json.dumps(images), content_type="application/json")


def inline_save(request):
    # print request.POST.get('content')
    if request.POST:
        app = request.POST.get('otc').split('-')[0]
        model_name = request.POST.get('otc').split('-')[1]
        id = request.POST.get('otc').split('-')[2]
        field = request.POST.get('otc').split('-')[3]
        model = apps.get_model(app, model_name)
        obj = model.objects.get(pk=id)
        setattr(obj,field,request.POST.get('content'))
        obj.save()
        return HttpResponse(json.dumps({'success': 'yes'}), content_type="application/json")
    return HttpResponse(json.dumps({'success': 'no'}), content_type="application/json")