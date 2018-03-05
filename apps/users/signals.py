# from .models import DefaultUser

# from django.conf import settings
# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
# from portal.utils import unique_slug_generator


# @receiver(pre_save, sender=DefaultUser)
# def default_user_pre_save_reciever(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)


# # @receiver(pre_save, sender=User)
# # def user_pre_save_reciever(sender, instance, *args, **kwargs):
#     # DefaultUser.objects.create(user=instance)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def user_post_save_save_reciever(sender, instance, created, *args, **kwargs):
#     print('post user save ....')
#     print('created: ')
#     print(created)
#     if created:
#         DefaultUser.objects.get_or_create(user=instance)
#     instance.defaultuser.save()
