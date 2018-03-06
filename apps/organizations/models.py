from django.db import models
from django.conf import settings
from django.urls import reverse


class Address(models.Model):
    """docstring for Adress"""
    street = models.CharField(max_length=255, null=False, blank=False, default=None)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=False, blank=False, default=None)
    province = models.CharField(max_length=2, null=False, blank=False, default=None)
    postalcode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=2, null=False, blank=False, default=None)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50)

    @property
    def title(self):
        return self.street

    def __str__(self):
        return self.street


class Company(models.Model):
    """docstring for Company"""
    name = models.CharField(max_length=255, null=False, blank=False,)
    contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,)
    address = models.ForeignKey(Address, models.SET_NULL, blank=True, null=True,)
    description = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, blank=True, null=True,)

    def get_absolute_url(self):
        return reverse('organizations:company_details', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name

    def __str__(self):
        return self.name
