from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver
from django.urls import reverse  # , reverse_lazy

from apps.issues.models import Issue
from portal.utils import unique_slug_generator


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    short_text = models.CharField(max_length=255, null=False, blank=False, default='',)
    comment = models.TextField(null=True, blank=True, default='',)
    issue = models.ForeignKey(Issue, related_name='comments', on_delete=models.CASCADE)

    # attachment = models.ImageField()

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('comments:comment_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.short_text

    @property
    def title(self):
        return self.name

    @property
    def owner(self):
        return self.user


def download_media_location(instance, filename):
    return "%/%s" % (instance.id, filename)


class File(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, default='',)
    description = models.TextField(null=True, blank=True, default='',)
    extension = models.CharField(max_length=25, null=True, blank=True, default='',)
    comment = models.ForeignKey(Comment, related_name='files', on_delete=models.CASCADE)
    attachment = models.FileField(null=True, blank=True, upload_to=download_media_location)

    # attachment = models.ImageField()

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('comments:comment_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.short_text


@receiver(pre_save, sender=Comment)
def comment_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=File)
def image_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
