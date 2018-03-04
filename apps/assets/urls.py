from django.urls import path
from .views import AssetListView

app_name = 'assets'
urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    # path('gates', AssetListView.as_view(), name='gate'),
    # path('doors', AssetListView.as_view(), name='door'),
    # path('access', AssetListView.as_view(), name='access'),
]
