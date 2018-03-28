
import random
import string
import os
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver
from django.utils.timezone import now as timezone_now
# from django.urls import reverse  # , reverse_lazy

from portal.utils import unique_slug_generator


def create_random_string(length=30):
    if length <= 0:
        length = 30

    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(symbols) for x in range(length)])


def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'my_uploads/{}_{}{}'.format(
        now.strftime("%Y/%m/%d/%Y%m%d%H%M%S"),
        create_random_string(),
        filename_ext.lower()
    )


class ImageQueryset(models.query.QuerySet):
    def for_instance(self, instance, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        return self.filter(content_type=content_type, object_id=object_id)


class ImageManager(models.Manager):
    def get_queryset(self):
        return FileQueryset(self.model, using=self._db)

    def for_instance(self, instance):
        return self.get_queryset().for_instance(instance)


class FileQueryset(models.query.QuerySet):
    def for_instance(self, instance, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        return self.filter(content_type=content_type, object_id=object_id)


class FileManager(models.Manager):
    def get_queryset(self):
        return FileQueryset(self.model, using=self._db)

    def for_instance(self, instance):
        return self.get_queryset().for_instance(instance)


class File(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True, default='',)
    extension = models.CharField(max_length=25, null=True, blank=True, default='',)
    description = models.TextField(null=True, blank=True, default='',)

    attachment = models.FileField(upload_to=upload_to, null=True, blank=True)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, related_name='files', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # issue []
    # comment []
    # asset []
    # site [profile image | map]
    # company [profile image | map]
    # user [profile image]

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    objects = FileManager()

    def __str__(self):
        return self.title


class FileAttachment(models.Model):
    attachment = models.FileField(upload_to=upload_to)
    filename = models.CharField(max_length=255, null=True, blank=True, default='',)
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='attachments')

    def __str__(self):
        return str(self.filename)


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False, default='',)
    extension = models.CharField(max_length=25, null=True, blank=True, default='',)
    description = models.TextField(null=True, blank=True, default='',)

    # attachment = models.ImageField()

    # # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, related_name='images', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    objects = ImageManager()

    def __str__(self):
        return self.title


@receiver(pre_save, sender=File)
def file_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Image)
def image_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
