from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save  # , post_save
from django.dispatch import receiver
from portal.utils import unique_slug_generator


class CommentManager(models.Manager):
    # def all(self):
    #     qs = super(CommentManager, self).filter(parent=None)
    #     return qs

    def for_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        print('content_type: ', content_type, ' | obj_id: ', obj_id)
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        print('QS: ', qs)
        return qs


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    # url = models.URLField()  # not a path, full url http://www.srvup.com/projects/1
    short_text = models.CharField(max_length=255, null=False, blank=False, default='',)
    content = models.TextField()
    # image       = models.ImageField()
    allow_anonymous = models.BooleanField(default=False)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, related_name='comments', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    objects = CommentManager()

    def __str__(self):
        if self.slug:
            return self.slug
        return self.content

    @property
    def owner(self):
        return self.user

    @property
    def title(self):
        return self.short_text


@receiver(pre_save, sender=Comment)
def comment_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
