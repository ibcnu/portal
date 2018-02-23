from django.urls import path
from apps.assets.views import AssetListView

urlpatterns = [
    path('', AssetListView.as_view(), name='profile'),
    path('gates', AssetListView.as_view(), name='gate'),
    path('doors', AssetListView.as_view(), name='door'),
    path('access', AssetListView.as_view(), name='access'),
]
