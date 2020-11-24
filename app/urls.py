from django.urls import path
from . import views
 
app_name = 'app'

urlpatterns = [
    path('top/', views.index, name='index'),
    path('player/', views.player, name='player'),
    path('cut/', views.Upload.as_view(), name='cut'),
    path('upload/', views.SingleUploadWithModelView.as_view(), name='upload'),
    path('', views.FileListView.as_view(), name='file_list'),
]
