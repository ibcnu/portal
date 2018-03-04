from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserProfiles(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    # fullname = models.CharField(max_length=255)

    def __str__(self):
        return 'nothing to see yet'


class UserSettings(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return 'nothing to see yet'
