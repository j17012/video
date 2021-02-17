from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import  UploadForm, UploadFormSet, UploadMultiForm
from .models import UploadFile, UploadImage, Label_Info
from . import cuts
from io import TextIOWrapper, StringIO
from django_pandas.io import read_frame
import csv
import json
import requests
import io
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from datetime import datetime as dt 
import os.path

matplotlib.use('Agg')


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
# 動画アップロード
class UploadView(generic.CreateView):
    # ファイルモデルのアップロードビュー
    model = UploadFile
    form_class = UploadForm
    template_name = 'app/upload.html'
    success_url = reverse_lazy('app:file_list')

# アップロード済み動画ファイル一覧
class FileListView(generic.ListView):
    #アップロードされたファイルの一覧ページ
    model = UploadFile

# アップロード済み画像ファイル一覧
class ImageListView(generic.ListView):
    # アップロードされたファイルの一覧ページ
    model = UploadImage


# ラベル情報一覧(テーブル情報のみ表示)
def label_list(request):
    data = Label_Info.objects.all()
    params = {'data':data}
    return render(request,'app/label_list.html',params)


# ラベルアップロード画面
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


def setPlt():
    # 格納されているラベル情報を全件取得
    data = Label_Info.objects.all()

    # DataFrameの形式に変換する 第1引数にQuerySetデータ、fieldnamesに取得したいカラムをリスト形式で指定
    df = read_frame(data, fieldnames=['man', 'pc_char', 'white_board','char_red','char_yellow','human_char'])

    """
    labels = ['man', 'pc_char', 'white_board','char_red','char_yellow','human_char']

    man = np.array(df.man)
    pc_char = np.array(df.pc_char)
    white_board = np.array(df.white_board)
    char_red = np.array(df_char.red)
    char_yellow = np.array(df.char_yellow)
    human_char = np.array(df.human_char)
    """
    
    # 積み上げ棒グラフを描画
    ax = df.plot.barh(stacked=True, figsize=(10.5,2),  color={'man': 'fuchsia', 'pc_char': 'yellow', 'white_board': 'darkviolet', 'char_red': 'green', 'char_yellow': 'orange', 'human_char': 'red'})
    ax.xaxis.set_visible(False)
    ax.invert_yaxis()
    """
    # 積み上げ棒グラフ
     # 'man', 'pc_char', 'white_board','char_red','char_yellow','human_char'
    # [[man], [pc_char], [white_board], [char_red], [char_yellow], [human_char]
    #[Label_Info.sec for Label_Info in data],[Label_Info.pc_char for Label_Info in data],[white_board],[char_red],[char_yellow],[human_char]
    # [100, 200, 50, 30, 40, 60], [30, 40, 60, 10, 20, 50], [50, 30, 60, 30, 40, 60], [100, 20, 30, 40, 60, 70], [30, 40, 60, 30, 40, 60], [50, 30, 60, 30, 40, 60]

    df = pd.DataFrame([[100, 200, 50, 30, 40, 60], [30, 40, 60, 10, 20, 50], [50, 30, 60, 30, 40, 60], [100, 20, 30, 40, 60, 70], [30, 40, 60, 30, 40, 60], [50, 30, 60, 30, 40, 60]],
                            index = ['man', 'pc_char', 'white_board','char_red','char_yellow','human_char'])

    plot_df = pd.DataFrame(index = df.index)
    for col in df.columns:
        plot_df[col] = round(100 * df[col] / df[col] / df[col].sum(),1)

    fig, ax = plt.subplots(figsize=(11, 2))
    for i in range(len(df)):
        ax.bar(df.columns, df.iloc[i], bottom=df.iloc[:i].sum())
    ax.legend(df.index)
    """

    """
    # グラフの色を設定する
    colors = ["red", "orange", "green", "darkviolet","yellow", "fuchsia"]
    
    x = [1, 2, 3, 4 ,5, 6]
    y = [6, 6, 6, 6, 6, 6]

    label_x = ["human_char", "char_yellow", "char_red", "white_board", "pc_char", "man"]

    # グラフを生成する範囲
    plt.figure(figsize = (11.5, 2))

    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.yaxis.label.set_color(colors)

    # 横棒グラフ生成
    plt.barh(x, y, color = colors)

    plt.yticks(x, label_x)  # X軸のラベル
    """
# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight', transparent=True)
    s = buf.getvalue()
    buf.close()
    return s
# 横棒グラフを描画
def get_svg(request):
    setPlt()  
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

#グラフ作成
def setPlt2():
    # 格納されているラベル情報を全件取得
    data = Label_Info.objects.all()
    # 各ラベル情報を取得
    sec = [ Label_Info.sec for Label_Info in data]
    man = [ Label_Info.man for Label_Info in data ]
    pc_char = [Label_Info.pc_char for Label_Info in data ]
    white_board = [ Label_Info.white_board for Label_Info in data ]
    char_red = [Label_Info.char_red for Label_Info in data ]
    char_yellow = [Label_Info.char_yellow for Label_Info in data]
    human_char = [Label_Info.human_char for Label_Info in data ]

    # グラフを生成する範囲
    plt.figure(figsize = (12.5, 2))

    #green", "darkviolet","yellow", "fuchsia"

    # 折れ線グラフ(プロットするデータ,線の太さ,色,ラベル名)
    plt.plot(man,lw=4,color="fuchsia",label="man")
    plt.plot(pc_char,lw=4,color="yellow",label="pc_char")
    plt.plot(white_board,lw=4,color="darkviolet",label="white_board")
    plt.plot(char_red,lw=4,color="green",label="char_red")
    plt.plot(char_yellow,lw=4,color="orange",label="char_yellow")
    plt.plot(human_char,lw=4,color="blue",label="human_char")
    

    """
    # 直線グラフ
    X = np.arange(0,11,1)
    Y = np.arange(0,11,1)
    F = np.array([0,0,0,0,0,0,1,1,0,1,0])

    # １線分ずつ色を変えてplotする
    for i in range(len(X)):
        plt.plot(X[i:i+2], Y[i:i+2], color= 'red' if F[i] == 0 else 'blue')
    """

# SVG化
def plt3svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight', transparent=True)
    s = buf.getvalue()
    buf.close()
    return s
# 折れ線グラフを描画
def get_svg2(request):
    setPlt2()  
    svg = plt3svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response