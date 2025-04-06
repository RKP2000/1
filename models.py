from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=50, null=False, unique=True)
    government_type = models.CharField(max_length=50, null=True)
    important_sports = models.TextField(max_length=200, null=True, blank=True)
    products= models.TextField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




