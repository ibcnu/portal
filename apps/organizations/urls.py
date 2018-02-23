from django.urls import path
from apps.organizations.views import CompanyListView

urlpatterns = [
    path('', CompanyListView.as_view(), name='profile'),
]
