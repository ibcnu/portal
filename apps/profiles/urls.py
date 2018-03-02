from django.urls import path
# from django.views.generic import TemplateView
from apps.profiles.views import ProfileView, SettingsView

urlpatterns = [
    path('', ProfileView.as_view(), name='profiles_profile'),
    path('settings', SettingsView.as_view(), name='profiles_settings'),
]
