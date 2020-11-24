from django import forms
from django.core.files.storage import default_storage
from .models import UploadFile


class SingleUploadModelForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = '__all__'

