from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import  SingleUploadModelForm
from .cuts import UploadForm
from .models import UploadFile
from . import cuts

def index(request):
    return render(request, 'app/index.html')

def player(request):
    return render(request, 'app/player.html')

def cut(request):
    return render(request, 'app/cut.html')

#動画分割
class Upload(generic.FormView):
    form_class = UploadForm
    template_name = 'app/cut.html'

    def form_valid(self, form):
        download_url = form.save()
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)
    
    def call_save_frames(request):
        if request.method == 'POST':
            #cut.pyのsave_framesを呼び出す
            #ajaxで送信したデータのうちimput_dataを指定して取得する
            cuts.save_frames(request.POST.get("imput_data"))
            return HttpResponse()

#動画アップロード
class SingleUploadWithModelView(generic.CreateView):
    #ファイルモデルのアップロードビュー
    model = UploadFile
    form_class = SingleUploadModelForm
    template_name = 'app/upload.html'
    success_url = reverse_lazy('app:file_list')

class FileListView(generic.ListView):
    #アップロードされたファイルの一覧ページ
    model = UploadFile