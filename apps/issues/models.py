from django.db import models
from apps.assets.models import Asset


class IssueType(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def __init__(self, arg):
    #     super(IssueType, self).__init__()
    #     self.arg = arg


class IssueStatus(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    # def __init__(self, arg):
    #     super(IssueStatus, self).__init__()
    #     self.arg = arg


class Issue(models.Model):
    """docstring for Company"""
    title = models.CharField(max_length=255)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    issuetype = models.ForeignKey(IssueType, on_delete=models.SET_NULL, blank=True, null=True,)
    status = models.ForeignKey(IssueStatus, on_delete=models.SET_NULL, blank=True, null=True,)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def __init__(self, arg):
    #     super(Asset, self).__init__()
    #     self.arg = arg


class UserIssueStatus(models.Model):
    """docstring for UserIssueStatus"""

    # def __init__(self, arg):
    #     super(UserIssueStatus, self).__init__()
    #     self.arg = arg
