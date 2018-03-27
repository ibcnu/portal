# from django.contrib.admNamein import register
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver
from django.urls import reverse  # , reverse_lazy

# from django.template.Library import inclusion_tag

from apps.organizations.models import Company
from portal.utils import unique_slug_generator


class AssetType(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True, default='',)
    value = models.CharField(max_length=255, null=True, blank=True, default='',)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    @property
    def title(self):
        return self.name

    def __str__(self):
        if self.value:
            return self.value
        else:
            return self.name


class AssetQueryset(models.query.QuerySet):
    def issues(self, *args, **kwargs):
        return self.filter(issues=kwargs.get())


class AssetModel(models.Manager):
    def get_queryset(self):
        return AssetQueryset(self.model, using=self._db)

    def issues(self, *args, **kwargs):
        return self.get_queryset.issues(*args, **kwargs)


class AssetManager(models.Manager):
    """docstring for AssetManager"""

    def all(self, *args, **kwargs):
        return super()

    def forCompany(self, id, *args, **kwargs):
        return super().filter()


class Asset(models.Model):
    """docstring for Company"""
    objects = AssetManager

    name = models.CharField(max_length=255, null=False, blank=False,)
    company = models.ForeignKey(Company, related_name='assets', on_delete=models.CASCADE, null=True, blank=True, )
    assettype = models.ForeignKey(AssetType, on_delete=models.SET_NULL, blank=True, null=True, )
    pid = models.CharField(max_length=255, null=True, blank=True, default='',)
    customerid = models.CharField(max_length=255, null=True, blank=True, default='',)
    description = models.TextField(null=True, blank=True, default='',)
    # assetusers = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     through='AssetUser',
    #     through_fields=('asset', 'user'),
    #     blank=True,
    # )

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True, default='',)

    def get_absolute_url(self):
        return reverse('assets:asset_details', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name

    def __str__(self):
        return self.name

    # @classmethod
    def add_user_to_asset(self, user):
        self.users.add(user)

    # @classmethod
    def remove_user_from_asset(self, user):
        self.users.remove(user)


# class AssetUser(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assets', on_delete=models.CASCADE)
#     asset = models.ForeignKey(Asset, related_name='assets', on_delete=models.CASCADE)
#     read = models.BooleanField(default=False)

#     @classmethod
#     def add_user_to_asset(cls, asset, user):
#         assetusers, created = cls.objects.get_or_create(
#             asset=asset
#         )
#         assetusers.user.add(user)

#     @classmethod
#     def remove_user_from_asset(cls, asset, user):
#         assetusers, created = cls.objects.get_or_create(
#             asset=asset
#         )
#         assetusers.user.remove(user)

#     @classmethod
#     def list_users_to_asset(cls, asset, user):
#         assetusers, created = cls.objects.get_or_create(
#             asset=asset
#         )
#         return assetusers.user.all()


@receiver(pre_save, sender=AssetType)
def asset_type_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Asset)
def asset_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# @register.inclusion_tag('asset_menu.html')
def load_asset_menu():
    assettypes = AssetType.choice_set.all()
    context = {
        'url': 'assets:asset_list',
        'li': assettypes,
    }
    return context
