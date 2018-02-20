from django.db import models


class Company(models.Model):
    """docstring for Company"""

    def __init__(self, arg):
        super(Company, self).__init__()
        self.arg = arg
