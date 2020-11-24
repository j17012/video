from django.urls import path
from . import views
 
app_name = 'app'

urlpatterns = [
    path('top/', views.index, name='index'),
    path('player/', views.player, name='player'),
    path('cut/', views.Upload.as_view(), name='cut'),
<<<<<<< HEAD
    path('upload/', views.SingleUploadWithModelView.as_view(), name='upload'),
    path('', views.FileListView.as_view(), name='file_list'),
=======
    path('upload/', views.UploadView.as_view(), name='upload'),
    path("ajax/", views.call_save_frames,name="call_save_frames")
>>>>>>> 14383aa0fe9ec94706f89a7ad9fa40ef2c374213
]
