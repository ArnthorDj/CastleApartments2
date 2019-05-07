from django.db import models

<<<<<<< HEAD
# Create your models here.
=======

class Members(models.Model):
    profile_image = models.CharField(max_length=999)
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=255)
>>>>>>> benjamin2
