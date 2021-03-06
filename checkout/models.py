from decimal import Decimal
from django.db import models
from artifacts.models import Artifact


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    county = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "Order Number {0} on {1} for {2}".format(self.id,
                                                        self.date,
                                                        self.full_name)


class PurchasedArtifact(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    artifact = models.ForeignKey(Artifact,
                                 on_delete=models.CASCADE,
                                 null=False)

    def __str__(self):
        price = self.artifact.purchase_price
        return f'{self.artifact.name} @ £{price:.2f}'
