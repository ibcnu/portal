from django.conf import settings
from django import forms
from apps.accounts.models import User
from .models import DefaultUser, UserRole
from apps.organizations.models import Company

# User = settings.AUTH_USER_MODEL


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('UserForm:KWARGS: ', kwargs)
        # instance = kwargs.get('instance')
        # print('UserForm:INSTANCE: ', instance)
        # if instance:
        #     self.fields['contact'].queryset = User.objects.filter(user_profile__in=instance.users.all())

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'fullname',
            'email',
            'password1',
            'password2',
            'is_active',
        ]


class CreateProfileForm(forms.Form):
    # photo = FileField(verbose_name =_("Profile Picture"), upload_to=upload_to("main.UserProfile.photo", "profiles"), format="Image", max_length=255, null=True, blank=True)
    # website = forms.URLField()

    phone = forms.CharField(max_length=20, required=False)
    city = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=False)

    company = forms.ModelChoiceField(Company.objects.all(), required=False)
    role = forms.ModelChoiceField(UserRole.objects.all(), required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = DefaultUser
        fields = [
            'bio',
            'phone',
            'city',
            'country',
            'role',
            'company',
            # 'slug',
        ]

    def clean_bio(self):
        pass


class UserRoleCreateForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['name', ]

    def clean_name(self):
        name = self.clean_data.get("name")
        if name == "hello":
            raise forms.ValidationError("not a valid name")
        return name
