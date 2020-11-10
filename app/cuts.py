import cv2
import os
from os.path import splitext, dirname, basename, join
from django import forms
from django.core.files.storage import default_storage




class UploadForm(forms.Form):
    file = forms.FileField(label='動画ファイル')

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)

    