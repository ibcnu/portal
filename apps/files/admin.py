from django.contrib import admin
from .models import File, Image, FileAttachment

admin.site.register(File)
admin.site.register(Image)
admin.site.register(FileAttachment)
