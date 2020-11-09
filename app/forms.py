from django import forms
from django.core.files.storage import default_storage
from .models import UploadFile


class SingleUploadForm(forms.Form):
    file = forms.FileField(label='動画ファイル')

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)


