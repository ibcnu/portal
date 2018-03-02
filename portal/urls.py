# from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView

from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('account/', include('apps.accounts.urls')),  # , namespace='accounts'

    path('profile/', include('apps.profiles.urls')),
    path('company/', include('apps.organizations.urls')),

    path('report/', include('apps.issues.urls')),

    path('asset/', include('apps.assets.urls')),

    path('user/', include('apps.users.urls')),

]
