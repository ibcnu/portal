from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver
from portal.utils import unique_slug_generator

# comments via urls and users


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField()  # not a path, full url http://www.srvup.com/projects/1
    short_text = models.CharField(max_length=255, null=False, blank=False, default='',)
    content = models.TextField()
    # image       = models.ImageField()
    allow_annon = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.url

    @property
    def owner(self):
        return self.user


@receiver(pre_save, sender=Comment)
def comment_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
