from django import forms
from django.core.files.storage import default_storage
from .models import UploadFile, UploadImage


class UploadForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = '__all__'

class UploadMultiForm(forms.ModelForm):

    class Meta:
        model = UploadImage
        fields = '__all__'

UploadFormSet = forms.modelformset_factory(
    UploadImage, form=UploadMultiForm,
    extra=5
)