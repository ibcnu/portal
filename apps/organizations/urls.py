from django.urls import path
from apps.organizations.views import CompanyListView, CompanyDetailView, CompanyCreateView

app_name = 'organizations'
urlpatterns = [
    path('', CompanyListView.as_view(), name='company_list'),
    path('<slug:slug>/', CompanyDetailView.as_view(), name='company_details'),
    path('create/', CompanyCreateView.as_view(), name='company_create'),
]
