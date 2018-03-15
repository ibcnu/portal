from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse

from portal.utils import unique_slug_generator
from apps.organizations.models import Company
# from apps.accounts.models import User
from apps.assets.models import Asset


class UserRole(models.Model):
    """docstring for UserRole"""
    name = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
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


class DefaultUser(models.Model):
    """docstring for Company"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile', on_delete=models.CASCADE)
    assets = models.ManyToManyField(Asset, related_name='users', blank=True, null=True,)
    # photo = models.FileField(verbose_name=_("Profile Picture"), upload_to=upload_to("main.UserProfile.photo", "profiles"), format="Image", max_length=255, null=True, blank=True)
    website = models.URLField(default='', blank=True, null=True,)
    bio = models.TextField(default='', blank=True, null=True,)
    phone = models.CharField(max_length=20, default='', blank=True, null=True,)
    city = models.CharField(max_length=100, default='', blank=True, null=True,)
    country = models.CharField(max_length=100, default='', blank=True, null=True,)
    company = models.ForeignKey(Company, related_name='users', on_delete=models.SET_NULL, blank=True, null=True,)  # organization
    role = models.ForeignKey(UserRole, related_name='users', on_delete=models.SET_NULL, blank=True, null=True,)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('users:user_detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.user.fullname

    def __str__(self):
        #     pass
        if self.user.fullname:
            return self.user.fullname
        else:
            return self.slug


class AdminUser(DefaultUser):
    """docstring for AdminUser"""
    # issubclass & isinstance


@receiver(pre_save, sender=DefaultUser)
def default_user_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# @receiver(pre_save, sender=User)
# def user_pre_save_reciever(sender, instance, *args, **kwargs):
    # DefaultUser.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save_save_reciever(sender, instance, created, *args, **kwargs):
    print('post user save ....')
    print('created: ')
    print(created)
    # if created:
    DefaultUser.objects.get_or_create(user=instance)
    # instance.DefaultUserr.save()
