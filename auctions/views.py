from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Listing,watchlist


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_view(request):
    return render(request, "auctions/create.html")

def create_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        starting_bid = request.POST['starting_bid']
        image = request.POST['img']
        category = request.POST['category']
        current_user = request.user
        user = User.objects.get(pk=current_user.id)

        listing = Listing.objects.create(title=title, description=description, starting_bid=starting_bid, image=image, category=category, user=user)
        return HttpResponseRedirect(reverse('index'))

def listing(request,listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.user.is_authenticated:
        current_user = request.user
        user = User.objects.get(pk=current_user.id)
        exist_watchlist = watchlist.objects.filter(item=listing, buyer=user).count
        return render(request, "auctions/listing.html", {
            "info": listing,
            "message": exist_watchlist
        })
    else: 
        return render(request, "auctions/listing.html", {
            "info": listing
        })

def add_wishlist(request):
    item_id = request.POST['item_id']
    listing = Listing.objects.get(pk=item_id)

    current_user = request.user
    user = User.objects.get(pk=current_user.id)

    Watchlist = watchlist.objects.create(item=listing, buyer=user)
    return render(request, "auctions/listing.html", {
        "info": listing,
        "message": 1
    })

def remove_wishlist(request):
    item_id = request.POST['item_id']
    listing = Listing.objects.get(pk=item_id)

    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    Watchlist = watchlist.objects.filter(item=listing, buyer=user).delete()
    return render(request, "auctions/listing.html", {
        "info": listing,
        "message":0
    })

def watchlist_view(request):
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    all_watchlist = watchlist.objects.filter(buyer=user)
    return render(request, "auctions/watchlist.html", {
        "items": all_watchlist
    })