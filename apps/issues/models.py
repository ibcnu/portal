from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from portal.utils import unique_slug_generator
from django.urls import reverse
from django.conf import settings
User = settings.AUTH_USER_MODEL

from apps.assets.models import Asset


class IssueType(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)
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


class IssueStatus(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)
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


class Issue(models.Model):
    """docstring for Company"""
    title = models.CharField(max_length=255)
    asset = models.ForeignKey(Asset, related_name='issues', on_delete=models.CASCADE)
    issuetype = models.ForeignKey(IssueType, related_name='issues', on_delete=models.SET_NULL, blank=True, null=True,)
    status = models.ForeignKey(IssueStatus, related_name='issues', on_delete=models.SET_NULL, blank=True, null=True,)
    description = models.TextField(blank=True, null=True, default='')
    summary = models.TextField(blank=True, null=True, default='')

    createdby = models.ForeignKey(User, related_name='issues', on_delete=models.SET_NULL, blank=True, null=True, )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('issues:issue_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    # def __init__(self, arg):
    #     super(Asset, self).__init__()
    #     self.arg = arg


class UserIssueStatus(models.Model):
    """docstring for UserIssueStatus"""

    # def __init__(self, arg):
    #     super(UserIssueStatus, self).__init__()
    #     self.arg = arg


@receiver(pre_save, sender=IssueType)
def issue_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=IssueStatus)
def status_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
