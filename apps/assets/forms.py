from django import forms
from .models import AssetType, Asset


class AssetTypeCreateForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = ['name', ]


class AssetCreateForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'name',
            'company',
            'assettype',
            'pid',
            'customerid',
            'description',
            'slug',
        ]
