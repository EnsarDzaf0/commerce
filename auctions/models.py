
from distutils.command.upload import upload
from email.policy import default
from unicodedata import decimal
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=6 ,decimal_places=2)
    image = models.ImageField(upload_to = "media")
    category = models.CharField(
        max_length=10
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_listings', default=None)
    current_price = models.DecimalField(max_digits=6 ,decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, related_name="listingwinner", default=None, on_delete=models.SET_NULL, null=True)

class watchlist(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name="itemwatchlist")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyerwatchlist")

class bids(models.Model):
    bid_item = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name="itembid")
    bid_buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyerbid")
    bid_amount = models.DecimalField(max_digits=6 ,decimal_places=2, default=0.00)