from django.urls import path
from .views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView

app_name = 'organizations'
urlpatterns = [
    path('', CompanyListView.as_view(), name='company_list'),
    path('create/', CompanyCreateView.as_view(), name='company_create'),
    path('edit/<slug:slug>/', CompanyUpdateView.as_view(), name='company_edit'),
    path('<slug:slug>/', CompanyDetailView.as_view(), name='company_details'),
]
