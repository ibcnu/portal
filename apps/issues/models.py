from django.db import models
from apps.assets.models import Asset


class IssueType(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)

    # def __init__(self, arg):
    #     super(IssueType, self).__init__()
    #     self.arg = arg


class IssueStatus(models.Model):
    """docstring for AssetType"""
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)

    # def __init__(self, arg):
    #     super(IssueStatus, self).__init__()
    #     self.arg = arg


class Issue(models.Model):
    """docstring for Company"""
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    issuetype = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    status = models.ForeignKey(IssueStatus, on_delete=models.CASCADE)

    # def __init__(self, arg):
    #     super(Asset, self).__init__()
    #     self.arg = arg


class UserIssueStatus(models.Model):
    """docstring for UserIssueStatus"""

    # def __init__(self, arg):
    #     super(UserIssueStatus, self).__init__()
    #     self.arg = arg
