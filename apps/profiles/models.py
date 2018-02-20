from django.db import models
from django.contrib.auth import get_user_model

# from apps.models import User
User = get_user_model()


class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
