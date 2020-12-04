from django.contrib import admin
from .models import UploadFile, UploadImage

admin.site.register(UploadFile)
admin.site.register(UploadImage)
