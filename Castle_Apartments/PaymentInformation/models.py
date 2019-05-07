from django.db import models


class CreditCard(models.Model):
    card_number = models.CharField(max_length=16)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    cvc = models.CharField(max_length=3)
