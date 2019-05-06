from django.db import models
from .Signup.models import Members
from .RealEstate.models import RealEstates
from .PaymentInformation.models import CreditCard


class Purchases(models.Model):
    buyer_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(RealEstates, on_delete=models.CASCADE)
    real_estate_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    card_information = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
