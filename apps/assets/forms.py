from django import forms
from .models import AssetType, Asset


class AssetTypeCreateForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = ['name', ]


class AssetCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('AssetCreateForm:ARGS: ', args)
        print('AssetCreateForm:KWARGS: ', kwargs)
        # print("AssetCreateForm:REQUEST: ", request)
        # instance = kwargs.get('instance')
        # print('UserForm:INSTANCE: ', instance)
        # if instance:
        #     self.fields['contact'].queryset = User.objects.filter(user_profile__in=instance.users.all())

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
        ]
