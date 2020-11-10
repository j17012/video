from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
#myapp/cuts.pyをインポートする
from . import cuts

from django.views import generic
from .forms import SingleUploadForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def cut(request):
    return render(request, 'cut.html')
def upload(request):
    return render(request, 'upload.html')
#ajaxでurlを指定したメソッド
def call_cut(request):
    if request.method =='GET':
       # cuts.pyのsave_frame()メソッドを呼び出す
       # ajaxで送信したデータのうち"input_data"を指定して取得する        
        cuts.save_frame(request.GET.get("input_data"))
        return HttpResponse()

#画像を表示
def cut(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request,'cut.html')

#ファイルアップロード
class SingleUploadView(generic.FormView):
    form_class = SingleUploadForm
    template_name = 'upload.html'

    def form_valid(self,form):
        download_url = form.save()
        context = {
                'download_url':download_url,
                'form':form,
                }
        return self.render_to_response(context)
