from django.urls import path

from .views import (
    landing, home, 
)

urlpatterns = [
    path('', landing, name='landing-page'),
    path('home/', home, name='home-page'),
]