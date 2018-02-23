from django.urls import path
# from django.views.generic import TemplateView
from apps.profiles.views import ProfileView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('settings', ProfileView.as_view(), name='profile'),
]
