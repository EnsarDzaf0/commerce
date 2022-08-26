from http.client import USE_PROXY
from django.contrib import admin

from .models import User,Listing,watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(watchlist)