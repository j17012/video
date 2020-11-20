from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.index, name='index'),
    path('player/', views.player, name='player'),
    path('cut/', views.Upload.as_view(), name='cut'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path("ajax/", views.call_save_frames,name="call_save_frames")
]
