from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Company(models.Model):
    """docstring for Company"""
    contact = models.OneToOneField(User, on_delete=models.CASCADE,)

    # def __init__(self, arg):
    #     super(Company, self).__init__()
    #     self.arg = arg
