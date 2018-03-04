from django.contrib import admin
from .models import IssueType, IssueStatus, Issue

admin.site.register(Issue)
admin.site.register(IssueStatus)
admin.site.register(IssueType)
