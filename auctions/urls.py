from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_view, name="create_view"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("watchlist", views.watchlist_view, name="watchlist_view"),
    path("wishlist", views.add_wishlist, name="wishlist"),
    path("unlist", views.remove_wishlist, name="unlist"),
    path("<int:listing_id>", views.listing, name="listing")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

