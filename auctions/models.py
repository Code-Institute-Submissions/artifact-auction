from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from artifacts.models import Artifact


class Auction(models.Model):
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20, default='Artifact Name')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    reserve_price = models.DecimalField(max_digits=11, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    def clean(self):
        if self.end_date is not None and self.start_date is not None and self.end_date < self.start_date:
            raise ValidationError('Auction end date must be after start date.')
        if self.end_date is not None and self.start_date is None:
            raise ValidationError('Enter start date or remove auction end date.')
        if self.artifact.sold is True:
            self.artifact = None
    
    def __str__(self):
        return self.artifact.name+" Auction"

@receiver(post_delete, sender=Auction)
def add_auction(sender, instance, **kwargs):
    instance.artifact.in_auction = False
    instance.artifact.save()