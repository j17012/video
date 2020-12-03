from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import  SingleUploadModelForm
from .models import UploadFile

def index(request):
    return render(request, 'app/index.html')

def player(request):
    return render(request, 'app/player.html')

#アップロード済み動画ファイル一覧
class FileListView(generic.ListView):
    #アップロードされたファイルの一覧ページ
    model = UploadFile
#動画アップロード
class SingleUploadWithModelView(generic.CreateView):
    #ファイルモデルのアップロードビュー
    model = UploadFile
    form_class = SingleUploadModelForm
    template_name = 'app/upload.html'
    success_url = reverse_lazy('app:file_list')
