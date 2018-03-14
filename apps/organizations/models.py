from django.db import models
from django.conf import settings
from django.urls import reverse
from portal.utils import unique_slug_generator

from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver

# from apps.users.models import DefaultUser


class Address(models.Model):
    """docstring for Adress"""
    street = models.CharField(max_length=255, null=False, blank=False, default=None)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True, default='')
    province = models.CharField(max_length=2, null=True, blank=True, default='')
    postalcode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True, default='')

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, blank=True, null=True,)

    @property
    def title(self):
        return self.street

    def __str__(self):
        return self.street


class Company(models.Model):
    """docstring for Company"""
    name = models.CharField(max_length=255, null=False, blank=False,)
    contact = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='company', on_delete=models.SET_NULL, blank=True, null=True,)
    address = models.OneToOneField(Address, related_name='company', on_delete=models.CASCADE, null=True, blank=True, )
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


@receiver(pre_save, sender=Company)
def company_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Address)
def address_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
