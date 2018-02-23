from django.urls import path
from apps.issues.views import IssueListView

urlpatterns = [
    path('', IssueListView.as_view()),
]
