from django import forms
from .models import Issue


class IssueCreateForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title',
            'asset',
            'issuetype',
            'status',
            'description',
            'summary',
            'slug',
        ]
