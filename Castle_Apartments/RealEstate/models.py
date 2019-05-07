from django.db import models

from Signup.models import Members


class RealEstateImages(models.Model):
    image1 = models.CharField(max_length=9999)


class RealEstates(models.Model):
    images = models.ForeignKey(RealEstateImages, on_delete=models.CASCADE)           # foreign key í aðra töflu með myndum
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=99)
    zip_code = models.CharField(max_length=3)           # m.v. Ísland, þriggja stafa póstnúmer
    size = models.CharField(max_length=10)              # fermetrar
    bedrooms = models.CharField(max_length=2)           # fjöldi svefnherbergja
    type = models.CharField(max_length=99)              # týpa af fasteign (einbýlishús, blokk, höll...)
    price = models.CharField(max_length=999)
    seller = models.ForeignKey(Members, on_delete=models.CASCADE)
    on_sale = models.BooleanField()

    # Approved
