from django import forms
from .models import File, Image


class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = [
            'user',
            'title',
            'description',
            'attachment',
            'content_type',
            'object_id',
            # 'content_object',
        ]

        widgets = {
            'attachment': forms.ClearableFileInput(attrs={'multiple': True}),
            'user': forms.HiddenInput(),
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
            'title': forms.HiddenInput(),
        }


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = [
            'user',
            'title',
            'description',
            # 'attachment',
            'content_type',
            'object_id',
            # 'content_object',
        ]

        widgets = {
            # 'user': forms.HiddenInput(),
            # 'content_type': forms.HiddenInput(),
            # 'object_id': forms.HiddenInput(),
        }
