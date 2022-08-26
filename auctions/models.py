
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

class watchlist(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name="itemwatchlist")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyerwatchlist")