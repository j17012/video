from django.contrib import admin
from .models import UploadFile, UploadImage, LabelInfo

admin.site.register(UploadFile)
admin.site.register(UploadImage)
admin.site.register(LabelInfo)
