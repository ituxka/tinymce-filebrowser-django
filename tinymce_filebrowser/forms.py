from django import forms

from .models import FileBrowserFile


class FileUploadForm(forms.ModelForm):
    """ File/Image Upload form """
    class Meta:
        model = FileBrowserFile
        fields = ('uploaded_file',)
