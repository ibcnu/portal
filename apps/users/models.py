from django.db import models
from apps.organizations.models import Company
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserRole(models.Model):
    """docstring for UserRole"""
    name = models.CharField(max_length=50, null=False, blank=False, primary_key=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __init__(self, arg):
        super(UserRole, self).__init__()
        self.arg = arg


class DefaultUser(models.Model):
    """docstring for Company"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    # photo = FileField(verbose_name =_("Profile Picture"), upload_to=upload_to("main.UserProfile.photo", "profiles"), format="Image", max_length=255, null=True, blank=True)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True,)
    # role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.fullname


class AdminUser(DefaultUser):
    """docstring for AdminUser"""
    # issubclass & isinstance

    def __init__(self, arg):
        super(AdminUser, self).__init__()
        self.arg = arg
