from django.conf import settings
from django import forms
from apps.accounts.models import User
from .models import DefaultUser, UserRole
from apps.organizations.models import Company

# User = settings.AUTH_USER_MODEL


class UserCreateForm(forms.ModelForm):
    # fullname = forms.CharField(label='Full Name')
    # email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    # photo = FileField(verbose_name =_("Profile Picture"), upload_to=upload_to("main.UserProfile.photo", "profiles"), format="Image", max_length=255, null=True, blank=True)
    # website = models.URLField(default='', blank=True)
    bio = forms.CharField(widget=forms.Textarea())
    phone = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    organization = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="")
    role = forms.ModelChoiceField(queryset=UserRole.objects.all(), empty_label='')
    slug = forms.SlugField()

    class Meta:
        model = User
        fields = [
            'fullname',
            'email',
            'password',
            'password2',
            'bio',
            'phone',
            'city',
            'country',
            'role',
            'organization',
            'slug',
        ]
        # exclude = ('user',)


class UserForm(forms.ModelForm):
    class Meta:
        model = DefaultUser
        fields = [
            'bio',
            'phone',
            'city',
            'country',
            'role',
            'organization',
            'slug',
        ]


class UserRoleCreateForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['name', ]

    def clean_name(self):
        pass
