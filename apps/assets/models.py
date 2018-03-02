from django.db import models
from apps.organizations.models import Company


class AssetType(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)


class Asset(models.Model):
    """docstring for Company"""
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assettype = models.ForeignKey(AssetType, on_delete=models.CASCADE)
