from django.conf import settings

from django import forms
from .models import AssetType, Asset  # , AssetUser
from apps.accounts.models import User

# User = settings.AUTH_USER_MODEL


class AssetTypeCreateForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = ['name', ]


class AssetCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AssetCreateForm, self).__init__(*args, **kwargs)
        print('AssetCreateForm:ARGS: ', args)
        print('AssetCreateForm:KWARGS: ', kwargs)
        instance = kwargs.get('instance')
        if instance:
            print('UserForm:INSTANCE: ', instance)
            print(instance.company.users.all())
            # self.fields['assetusers'].queryset = instance.company.users.all()

    # def save(self):
    #     print('saving')

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
            # 'assetusers',
        ]
        widgets = {
            'slug': forms.HiddenInput(),
            # 'assetusers': forms.CheckboxSelectMultiple()
        }


class AssetUserUpdateForm(forms.Form):

    def __init__(self, asset, *args, **kwargs):
        super(AssetUserUpdateForm, self).__init__(*args, **kwargs)
        print('AssetUserUpdateForm:KWARGS: ', kwargs)
        print('AssetUserUpdateForm:asset: ', asset)
        if asset:
            print('UserForm:INSTANCE: ', asset)
            print(asset.company.users.all())

        fullname = forms.CharField(max_length=255)
    # fullname = forms.CharField(max_length=255, forms.widgets.SelectMultiple())

    #     def __init__(self, *args, **kwargs):
    #         super(AssetUserUpdateForm, self).__init__(*args, **kwargs)
    #         print('AssetUserUpdateForm:ARGS: ', args)
    #         print('AssetUserUpdateForm:KWARGS: ', kwargs)
    #         instance = kwargs.get('instance')
    #         if instance:
    #             print('AssetUserUpdateForm:INSTANCE: ', instance)
    #             # print(instance.company.users.all())
    #             # self.fields['assetusers'].queryset = instance.company.users.all()

    #     # def save(self):
    #     #     print('saving')
