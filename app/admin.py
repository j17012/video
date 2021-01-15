from django.contrib import admin
from .models import UploadFile, UploadImage, Label_Info

admin.site.register(UploadFile)
admin.site.register(UploadImage)
admin.site.register(Label_Info)
