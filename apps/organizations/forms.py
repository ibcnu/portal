from django import forms

from .models import Company, Address
from apps.users.models import DefaultUser
from apps.accounts.models import User


class CompanyCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            qs = DefaultUser.objects.filter(organization=instance)  # groups__name='foo'
            qs2 = User.objects.filter(user_profile__in=qs)
            print('QS: ', qs)
            print('QS2: ', qs2)
            self.fields['contact'].queryset = qs2

    class Meta:
        model = Company
        fields = [
            'name',
            'contact',
            'address',
            'description',
            'slug',
        ]


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street',
            'street2',
            'city',
            'province',
            'postalcode',
            'country',
            'slug',
        ]
