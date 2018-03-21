from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):
    # widget=forms.TestInput(attrs={'class'='form-control', 'placeholder'='', 'id'='name'})
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = [
            'user',
            'short_text',
            'comment',
            'issue',
            'slug',
        ]
