from django.shortcuts import render
from .models import Image

global locations, categories
locations = ["Metropolis", "Gotham", "Central City", "Avengers mansion", "Bifrost", "Wakanda"]
categories = ["naruto", "dmc"]


def index(request):
    """
    Handles requests for the homepage
    renders index.html
    """
    title = 'Welcome'
    photos = Image.get_all()
    return render(request, 'index.html',
                  {"title": title,
                   "photos": photos,
                   "locations": locations,
                   "categories": categories})
