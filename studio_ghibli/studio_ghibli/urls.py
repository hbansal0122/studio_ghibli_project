"""studio_ghibli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.decorators.cache import cache_page
from django.urls import path, include, re_path
from movies.views import NotFound, MovieView
from constants import CACHE_TIMEOUT

urlpatterns = [
    path('movies/', cache_page(CACHE_TIMEOUT)(MovieView.as_view()), name='Studio'),
    re_path(r'(?s).*', NotFound.as_view(), name='Error'),
]
