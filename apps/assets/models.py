from django.db import models
from apps.organizations.models import Company


class AssetType(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255)


class Asset(models.Model):
    """docstring for Company"""
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
