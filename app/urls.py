from django.urls import path
from . import views
 
app_name = 'app'

urlpatterns = [
    path('top/', views.index, name='index'),
    path('player/', views.player, name='player'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('upload_image/', views.mulit_upload, name='upload_image'),
    path('file_list/', views.FileListView.as_view(), name='file_list'),
    path('image_list/', views.ImageListView.as_view(), name='image_list'),
    path('label_list/',views.label_list,name='label_list'),
    path('result/', views.result, name='result'),
    path('ajax/', views.call_cuts, name='call_cuts'),
    path('upload_label/',views.label,name='upload_label'),
    path('plot/', views.get_svg, name='plot'),
    path('plot2/', views.get_svg2, name='plot2'),
]
