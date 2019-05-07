from django.db import models


class Employees(models.Model):
    profile_image = models.CharField(max_length=999)
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    phone = models.CharField(max_length=12)
    email = models.Charfield(max_length=255)
    username = models.CharField(max_length=55)
    password = models.Charfield(max_length=55)
