from .models import Address, Company
from portal.utils import unique_slug_generator

from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver


@receiver(pre_save, sender=Company)
def company_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Address)
def address_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
