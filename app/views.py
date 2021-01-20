from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import  UploadForm, UploadFormSet, UploadMultiForm
from .models import UploadFile, UploadImage, Label_Info
from . import cuts
import csv
from io import TextIOWrapper, StringIO
import os.path

def index(request):
    return render(request, 'app/index.html')

def player(request):
    data = Label_Info.objects.all()
    params = {'data':data}
    return render(request,'app/player.html',params)

def result(request):
    return render(request, 'app/result.html')

def call_cuts(request):
    if request.method == 'POST':
        # cuts.pyのsave_frames()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        cuts.save_frames(request.POST.get("input_data"))
        #import pdb; pdb.set_trace()
        #print(request.POST.get("input_data"))
        return HttpResponse(reverse('app:result'))

#画像アップロード
def mulit_upload(request):
    formset = UploadFormSet(request.POST or None, files=request.FILES or None, queryset=UploadImage.objects.none())
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('app:image_list')

    context = {
        'form':formset
    }

    return render(request, 'app/upload.html', context)
#動画アップロード
class UploadView(generic.CreateView):
    #ファイルモデルのアップロードビュー
    model = UploadFile
    form_class = UploadForm
    template_name = 'app/upload.html'
    success_url = reverse_lazy('app:file_list')

#アップロード済み動画ファイル一覧
class FileListView(generic.ListView):
    #アップロードされたファイルの一覧ページ
    model = UploadFile

#アップロード済み画像ファイル一覧
class ImageListView(generic.ListView):
    #アップロードされたファイルの一覧ページ
    model = UploadImage

#ラベル情報一覧(テーブル情報のみ表示)
def label(request):
    data = Label_Info.objects.all()
    params = {'data':data}
    return render(request,'app/label_list.html',params)

#ラベル管理画面
def label_list(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            label = Label_Info()
            label.sec = line[0]
            label.man = line[1]
            label.pc_char = line[2]
            label.white_board = line[3]
            label.char_red = line[4]
            label.char_yellow = line[5]
            label.human_char = line[6]
            label.save()

        return render(request,'app/label_list.html')
    
    else:
        return render(request,'app/label_list.html')
