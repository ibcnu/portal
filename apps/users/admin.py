from django.contrib import admin
from .models import DefaultUser, UserRole


admin.site.register(DefaultUser)
admin.site.register(UserRole)
