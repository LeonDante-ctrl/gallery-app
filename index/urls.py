from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

"""
Import the project settings where we added the
template context processor that allows us to load our images.
Add the static function from django.conf.urls.static.
Configure our app url to register the MEDIA_ROOT route.
"""

urlpatterns = [
    path('', views.index, name='welcome'),
    path('search', views.search_results, name='search_results'),
    path('location/<loc>', views.get_image_by_location, name='location'),
    path('categories/<cat>', views.get_image_by_category, name='categories'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
