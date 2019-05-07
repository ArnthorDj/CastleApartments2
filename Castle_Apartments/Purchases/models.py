from django.db import models
from PaymentInformation.models import CreditCard
from RealEstate.models import RealEstates
from Signup.models import Members


class Purchases(models.Model):
    buyer_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    real_estate_id = models.ForeignKey(RealEstates, on_delete=models.CASCADE)
    card_information_id = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
