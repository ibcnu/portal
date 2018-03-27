from django.urls import path
from .views import (
    AssetListView, AssetCreateView, AssetUpdateView, AssetDetailView, AssetUsersView, asset_users_change_view  # , AssetUserUpdateView
    # AssetTypeCreateView,
)

app_name = 'assets'
urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    path('<atype>', AssetListView.as_view(), name='asset_list'),
    path('create/', AssetCreateView.as_view(), name='asset_create'),
    path('edit/<slug:slug>/', AssetUpdateView.as_view(), name='asset_edit'),
    # path('users/<int:pk>/', AssetUserUpdateView.as_view(), name='modify_users'),
    path('users/', AssetUsersView.as_view(), name='asset_users'),
    path('<slug:slug>/', AssetDetailView.as_view(), name='asset_details'),
    path('users/', AssetUsersView.as_view(), name='asset_users'),
    path('users/<str:operation>/<int:pk>/<int:asset_pk>/', asset_users_change_view, name='asset_change_users'),
    # path('type/', AssetTypeCreateView.as_view(), name='assettype_create'),

    # path('gates', AssetListView.as_view(), name='gate'),
    # path('doors', AssetListView.as_view(), name='door'),
    # path('access', AssetListView.as_view(), name='access'),
]
