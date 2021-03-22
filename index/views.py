from django.shortcuts import render
from .models import Image

global locations, categories
locations = ["Mali", "ichiraku", "leaf village", "soya park", "libashire", "Parleys"]
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


def search_results(request):
    """
    Handles search requests
    """
    if 'image' in request.GET and request.GET["image"]:
        query = request.GET.get("image")
        photos = Image.searched(query)
        message = f"{query}"

        return render(request, 'results.html',
                      {"message": message, "photos": photos, "locations": locations, "categories": categories})
    else:
        message = "What images are you looking for?"
        return render(request, 'results.html',
                      {"message": message, "locations": locations, "categories": categories})
