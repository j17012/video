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
    path('result/', views.result, name='result'),
    path('ajax/', views.call_cuts, name='call_cuts'),
    path('label_list/',views.label,name='label_list'),
]
