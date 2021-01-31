from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import  UploadForm, UploadFormSet, UploadMultiForm
from .models import UploadFile, UploadImage, Label_Info
from . import cuts
from io import TextIOWrapper, StringIO
import csv
import io
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt 
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

"""
#ラベル情報一覧(テーブル情報のみ表示)
def label(request):
    data = Label_Info.objects.all()
    params = {'data':data}
    return render(request,'app/label_list.html',params)
"""

#ラベルアップロード画面
def label(request):
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

        return render(request,'app/upload_label.html')
    
    else:
        return render(request,'app/upload_label.html')

#グラフ作成
def setPlt():
    #格納されているラベル情報を全件取得
    data = Label_Info.objects.all()
    #各ラベル情報を取得
    sec = [ Label_Info.sec for Label_Info in data]
    man = [ Label_Info.man for Label_Info in data ]
    pc_char = [Label_Info.pc_char for Label_Info in data ]
    white_board = [ Label_Info.white_board for Label_Info in data ]
    char_red = [Label_Info.char_red for Label_Info in data ]
    char_yellow = [Label_Info.char_yellow for Label_Info in data]
    human_char = [Label_Info.human_char for Label_Info in data ]

    """
    #Label_Infoのman,pc_char,white_board,char_red,char_yellow,human_charを変数で設定する記述をする
    x = [man,pc_char,white_board,char_red,char_yellow,human_char]
    #Label_Infoのsecをi:s(n分n秒)で設定する記述をする
    y = [sec]

    label_x = ["human_char","char_yellow", "char_red", "white_board", "pc_char", "man"]
    label_y = [sec]
    
    plt.barh(x,y)

    plt.yticks(x,label_x)  # X軸のラベル
    plt.xticks(y,label_y)   # y軸ラベル
    """
    #グラフを生成する範囲
    plt.figure(figsize=(12, 4))

    #折れ線グラフ
    plt.plot(man,linewidth=4,color="darkred",label="man")
    plt.plot(pc_char,linewidth=4,color="green")
    plt.plot(white_board,linewidth=4,color="orange")
    plt.plot(char_red,linewidth=4,color="red")
    plt.plot(char_yellow,linewidth=4,color="yellow")
    plt.plot(human_char,linewidth=4,color="blue")
    
    """
    #直線グラフ
    X = np.arange(0,11,1)
    Y = np.arange(0,11,1)
    F = np.array([0,0,0,0,0,0,1,1,0,1,0])

    # １線分ずつ色を変えてplotする
    for i in range(len(X)):
        plt.plot(X[i:i+2], Y[i:i+2], color= 'red' if F[i] == 0 else 'blue')
    """
    
# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数
def get_svg(request):
    setPlt()  
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response