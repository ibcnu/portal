from django.db import models
# from apps.organizations.models import Company
from django.contrib.auth import get_user_model
User = get_user_model()


class DefaultUser(models.Model):
    """docstring for Company"""

    # contact = models.OneToOneField(User, on_delete=models.CASCADE,)
    # company = models.OneToOneField(Company, on_delete=models.CASCADE)
    # fullname = models.CharField(max_length=255)


class AdminUser(DefaultUser):
    """docstring for AdminUser"""

    def __init__(self, arg):
        super(AdminUser, self).__init__()
        self.arg = arg
