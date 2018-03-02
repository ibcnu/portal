from django.db import models
from apps.organizations.models import Company


class DefaultUser(models.Model):
    """docstring for Company"""
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
