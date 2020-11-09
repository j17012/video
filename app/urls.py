from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.index, name='index'),
    path('player/', views.player, name='player'),
    path('cut/', views.SingleUpload.as_view(), name='cut'),
    path('upload/', views.SingleUploadView.as_view(), name='upload'),
]
