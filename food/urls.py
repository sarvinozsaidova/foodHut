from django.urls import path
from .views import food


urlpatterns = [
    path('', food, name='food'),
]