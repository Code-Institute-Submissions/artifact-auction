from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.name

class Artifact(models.Model):
    TYPE_CHOICES = [
        ('CULTURAL', "Cultural"), 
        ('MEDIA', "Media"),
        ('KNOWLEDGE', "Knowledge"),
        ('DATA', "Data")
    ]
    
    name = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=500, default='An artifact')
    image = models.ImageField(upload_to='images', null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0) #the buy now price or maximum bid price
    buy_now_price = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    sold = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    in_auction = models.BooleanField(default=False)

    def clean(self):
        if self.owner == None and self.sold == True:
            raise ValidationError('No owner, set sold to false or set owner.')
        if self.sold == False and self.owner is not None:
            raise ValidationError('Marked as sold, set owner to none or mark as sold.')

    def __str__(self):
        return self.name


