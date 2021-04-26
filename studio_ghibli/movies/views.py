from django.shortcuts import render
from django.views.generic import View
from .api_data.get_movie_data import get_movie_data
from .api_data.api import get_films, get_people


class NotFound(View):
    """Not found page for showing default error view"""
    def get(self, request, *args, **kwargs):
        return render(request, "error.html", context={})

class MovieView(View):
    """Get the movie data from ghibli api and pass to django template through context"""
    def get(self, request, *args, **kwargs):
        context = get_movie_data(films = get_films(), people = get_people())
        return render(request, "index.html", context=context)
            
