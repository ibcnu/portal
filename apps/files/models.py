# from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver
from django.urls import reverse  # , reverse_lazy

from portal.utils import unique_slug_generator


class FileQueryset(models.query.QuerySet):
    def for_instance(self, instance, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        return self.filter(content_type=content_type, object_id=object_id)


class FileManager(models.Manager):
    def get_queryset(self):
        return FileQueryset(self.model, using=self._db)

    def for_instance(self, instance):
        return self.for_instance(instance)


class File(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False, default='',)
    extension = models.CharField(max_length=25, null=True, blank=True, default='',)
    description = models.TextField(null=True, blank=True, default='',)

    # attachment = models.ImageField()

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

    def get_absolute_url(self):
        return reverse('comments:comment_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


@receiver(pre_save, sender=File)
def image_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
