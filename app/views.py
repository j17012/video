from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from .forms import SingleUploadForm
from . import cuts

def index(request):
    return render(request, 'app/index.html')

def player(request):
    return render(request, 'app/player.html')

def cut(request):
    return render(request, 'app/cut.html')
    
#動画分割
class SingleUpload(generic.FormView):
    form_class = SingleUploadForm
    template_name = 'app/cut.html'

    def form_valid(self, form):
        download_url = form.save()
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)

#動画アップロード
class SingleUploadView(generic.FormView):
    form_class = SingleUploadForm
    template_name = 'app/upload.html'

    def form_valid(self, form):
        download_url = form.save()
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)