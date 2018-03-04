from django import forms
from .models import Company


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'contact',
            'address',
            'description',
            'slug',
        ]

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     return name
