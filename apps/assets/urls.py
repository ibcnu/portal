from django.urls import path
from .views import (
    AssetListView, AssetCreateView, AssetUpdateView, AssetDetailView,
    # AssetTypeCreateView,
)

app_name = 'assets'
urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    path('create/', AssetCreateView.as_view(), name='asset_create'),
    path('edit/<slug:slug>/', AssetUpdateView.as_view(), name='asset_edit'),
    path('<slug:slug>/', AssetDetailView.as_view(), name='asset_details'),
    # path('type/', AssetTypeCreateView.as_view(), name='assettype_create'),

    # path('gates', AssetListView.as_view(), name='gate'),
    # path('doors', AssetListView.as_view(), name='door'),
    # path('access', AssetListView.as_view(), name='access'),
]
