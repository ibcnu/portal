from django.db import models
from django.contrib.auth import get_user_model
from django.utils.encoding import python_2_unicode_compatible
User = get_user_model()


@python_2_unicode_compatible
class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return 'nothing to see yet'
