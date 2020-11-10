from django.urls import path
from . import views

urlpatterns = [
        path('templates/', views.index, name='index'),
        path('cut/', views.cut, name='cut'),
        path('upload/',views.upload, name='upload'),
        path("ajax/",views.call_cut, name="call_cut"),
]

