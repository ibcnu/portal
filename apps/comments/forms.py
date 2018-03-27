from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'user',
            'short_text',
            # 'short_text',
            'content',
            'content_type',
            'object_id',
            # 'content_object',
        ]

        widgets = {
            'user': forms.HiddenInput(),
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
            # 'content_object': forms.HiddenInput(),
        }
