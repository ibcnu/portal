from django.urls import path
from apps.organizations.views import CompanyListView  # , CompanyDetailView

urlpatterns = [
    path('', CompanyListView.as_view(), name='company_list'),
    # path('<slug:slug>/', CompanyDetailView.as_view(), name='company_details'),
]
