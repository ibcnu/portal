from django.contrib import admin
from .models import Asset, AssetType

admin.site.register(AssetType)
admin.site.register(Asset)
