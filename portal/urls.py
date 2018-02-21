from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from portal.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('login', TemplateView.as_view(template_name=settings.CURRENT_TEMPLATE + '/login.html'), name='login'),
    path('reset', TemplateView.as_view(template_name=settings.CURRENT_TEMPLATE + '/reset.html'), name='reset'),
    path('logout', TemplateView.as_view(template_name=settings.CURRENT_TEMPLATE + '/login.html'), name='logout'),

    path('profile', include('apps.profiles.urls')),
    # path('settings', LoginView.as_view(), name='settings'),

    # path('company', LoginView.as_view(), name='companylist'),
    # path('user', LoginView.as_view(), name='userlist'),
    # path('report', LoginView.as_view(), name='report'),
    # path('assets', LoginView.as_view(), name='asset'),
    # path('assets/gate', LoginView.as_view(), name='gate'),
    # path('assets/door', LoginView.as_view(), name='door'),
    # path('assets/access', LoginView.as_view(), name='access'),


    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('', ),
    # path('', views.index, name='index'),
]
