from django.urls import path
from .views import (
    UserListView, UserDetailView, UserCreateView,
    UserRoleListView, UserUpdateView  # , UserNProfileUpdateView,
)

app_name = 'users'
urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('', UserListView.as_view(), name='user_list'),
    path('<slug:slug>/', UserDetailView.as_view(), name='user_detail'),
    path('edit/<slug:slug>/', UserUpdateView.as_view(), name='user_edit'),
    path('roles/', UserRoleListView.as_view(), name='userrole_list'),
]
