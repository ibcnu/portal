from django.urls import path
from .views import UserListView

app_name = 'users'
urlpatterns = [
    # path('', UserListView.as_view(), name='profile')
    path('', UserListView.as_view(), name='user_list')
]
