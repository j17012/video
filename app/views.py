from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import  UploadForm
from .models import UploadFile
from . import cuts

def index(request):
    return render(request, 'app/index.html')

def player(request):
    return render(request, 'app/player.html')

def call_cuts(request):
    if request.method == 'POST':
        # cuts.pyのsave_frames()メソッドを呼び出す。
        # ajaxで送信したデータのうち"id"を指定して取得する。
        cuts.save_frames(request.POST.get(id))
        return HttpResponse()

#アップロード済み動画ファイル一覧
class FileListView(generic.ListView):
    #アップロードされたファイルの一覧ページ
    model = UploadFile
#動画アップロード
class UploadView(generic.CreateView):
    #ファイルモデルのアップロードビュー
    model = UploadFile
    form_class = UploadForm
    template_name = 'app/upload.html'
    success_url = reverse_lazy('app:file_list')