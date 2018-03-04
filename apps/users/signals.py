

from .models import DefaultUser

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()


@receiver(pre_save, sender=User)
def user_pre_save_reciever(sender, instance, *args, **kwargs):
    print('saving ....')
    print(instance.timestamp)


@receiver(post_save, sender=User)
def user_post_save_create_reciever(sender, instance, created, *args, **kwargs):
    print('saving ....')
    print(instance.timestamp)
    if created:
        DefaultUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def user_post_save_save_reciever(sender, instance, created, *args, **kwargs):
    print('saving ....')
    print(instance.timestamp)
    instance.profile.save()
