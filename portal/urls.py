from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView

from .views import (SiteSettingsView, CompanyIndexView,)  # IndexView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', CompanyIndexView.as_view(), name='index'),
    # path('comments/', include('django_comments_xtd.urls'), name='comments'),
    path('settings', SiteSettingsView.as_view(), name='site_settings'),

    path('account/', include('apps.accounts.urls', namespace='accounts')),
    path('asset/', include('apps.assets.urls', namespace='assets')),
    path('company/', include('apps.organizations.urls', namespace='organizations')),
    path('profile/', include('apps.profiles.urls', namespace='profiles')),
    path('report/', include('apps.issues.urls', namespace='issues')),
    path('user/', include('apps.users.urls', namespace='users')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
