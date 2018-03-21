from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver
from django.urls import reverse  # , reverse_lazy

from apps.issues.models import Issue
from portal.utils import unique_slug_generator


class File(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False, default='',)
    extension = models.CharField(null=True, blank=True, default='',)
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
    def owner(self):
        return self.user


@receiver(pre_save, sender=File)
def image_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
