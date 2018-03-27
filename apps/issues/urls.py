from django.urls import path
from .views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView

app_name = 'issues'
urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('create/', IssueCreateView.as_view(), name='issue_create'),
    path('edit/<slug:slug>/', IssueUpdateView.as_view(), name='issue_edit'),
    path('<slug:slug>/', IssueDetailView, name='issue_details'),
    # path('<slug:slug>/', IssueDetailView.as_view(), name='issue_details'),
]
