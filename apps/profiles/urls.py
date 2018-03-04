from django.urls import path
# from django.views.generic import TemplateView
from .views import ProfileView, SettingsView

app_name = 'profiles'
urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('settings/', SettingsView.as_view(), name='settings'),
]
