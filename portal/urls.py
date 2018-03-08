# from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView

from .views import IndexView, SiteSettingsView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', IndexView.as_view(), name='index'),
    path('settings', SiteSettingsView.as_view(), name='site_settings'),

    path('account/', include('apps.accounts.urls', namespace='accounts')),
    path('asset/', include('apps.assets.urls', namespace='assets')),
    path('company/', include('apps.organizations.urls', namespace='organizations')),
    path('profile/', include('apps.profiles.urls', namespace='profiles')),
    path('report/', include('apps.issues.urls', namespace='issues')),
    path('user/', include('apps.users.urls', namespace='users')),

]
