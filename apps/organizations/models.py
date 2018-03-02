from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Address(models.Model):
    """docstring for Adress"""
    street = models.CharField(max_length=255, null=False, blank=False)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=False, blank=False)
    province = models.CharField(max_length=2, null=False, blank=False)
    postalcode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=2, null=False, blank=False)
    slug = models.SlugField

    def __init__(self, arg):
        super(Address, self).__init__()
        self.arg = arg


class Company(models.Model):
    """docstring for Company"""
    name = models.CharField(max_length=255)
    contact = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    # def __init__(self, arg):
    #     super(Company, self).__init__()
    #     self.arg = arg
