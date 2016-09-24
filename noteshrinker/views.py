from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from django.views.generic import CreateView, DeleteView, ListView
import json
from .models import Picture
from .response import JSONResponse, response_mimetype
from .serialize import serialize
from django.views.decorators.http import require_POST
from .noteshrink_module import AttrDict,notescan_main
from django.conf import settings
from django.http import HttpResponse
import os
@require_POST
def download(request):
    filename=request.POST['filename']
    file_path = os.path.join(settings.PDF_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404


def index(request):
    return render(request,'index.html')
#TODO:
# 1. Сделать чтобы сохранялись загруженные файлы по сессии
# 2. Удалять сразу не разрешенные файлы
#
#
@require_POST
def shrink(request):
    files = request.POST.getlist('files[]')
    existing_files = []
    for i in files:
        path = os.path.join(settings.MEDIA_ROOT,'pictures', i)
        if os.path.exists(path):
         existing_files.append(path)
    if len(existing_files)==0:
        return Http404
    options= {
    "basename": 'page', #базовое название для картинки
    "filenames": existing_files, #массив путей к файлам
    "global_palette": False, # одна палитра для всех картинок
    "num_colors": 8, #цветов на выходе
    "pdf_cmd": 'convert %i %o', # команда для пдф
    "pdfname": 'shrinked.pdf', #название выходного пдф файла
    "postprocess_cmd": None,
    "postprocess_ext": '_post.png', # название после процессинга (?)
    "quiet": False, # сократить выдачу
    "sample_fraction": 0.05, #пикселей брать за образец в %
    "sat_threshold": 0.2, #насыщенность фона
    "saturate": True, #насыщать
    "sort_numerically": True, # оставить порядок следования
    "value_threshold": 0.25, # пороговое значение фона
    "white_bg": False # белый фон
    }
    notescan_main(AttrDict(options))
    return JsonResponse(options)


class PictureCreateView(CreateView):
    model = Picture
    fields = "__all__"
    template_name = 'index.html'
    def form_valid(self, form):
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')



# class PictureDeleteView(DeleteView):
#     model = Picture
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.delete()
#         response = JSONResponse(True, mimetype=response_mimetype(request))
#         response['Content-Disposition'] = 'inline; filename=files.json'
#         return response

#
# class PictureListView(ListView):
#     model = Picture
#
#     def render_to_response(self, context, **response_kwargs):
#         files = [ serialize(p) for p in self.get_queryset() ]
#         data = {'files': files}
#         response = JSONResponse(data, mimetype=response_mimetype(self.request))
#         response['Content-Disposition'] = 'inline; filename=files.json'
#         return response
