from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return 'nothing to see yet'


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return 'nothing to see yet'
