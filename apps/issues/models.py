from apps.assets.models import Asset
from apps.comments.models import Comment
from apps.files.models import File, Image
# from .forms import IssueCreateForm

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse

from portal.utils import unique_slug_generator

User = settings.AUTH_USER_MODEL


class IssueType(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)
    value = models.CharField(max_length=255, null=True, blank=True, default='',)
    verbosevalue = models.CharField(max_length=255, null=True, blank=True, default='',)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, blank=True, null=True,)

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
    verbosevalue = models.CharField(max_length=255, null=True, blank=True, default='',)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, blank=True, null=True,)

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
    currentowner = models.ForeignKey(User, related_name='issues', on_delete=models.SET_NULL, blank=True, null=True, )

    createdby = models.ForeignKey(User, related_name='created_issues', on_delete=models.SET_NULL, blank=True, null=True, )
    # attachment

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, blank=True, null=True,)

    def get_absolute_url(self):
        return reverse('issues:issue_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    @property
    def files(self):
        return File.objects.for_instance(self)

    @property
    def images(self):
        return Image.objects.for_instance(self)

    @property
    def comments(self):
        return Comment.objects.for_instance(self)

    @property
    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__)


class UserIssueStatus(models.Model):
    # issue = models.ForeignKey(Issue, related_name='issues', on_delete=models.CASCADE)
    """docstring for UserIssueStatus"""

    # def __init__(self, arg):
    #     super(UserIssueStatus, self).__init__()
    #     self.arg = arg


@receiver(pre_save, sender=IssueType)
def type_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=IssueStatus)
def status_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Issue)
def issue_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
