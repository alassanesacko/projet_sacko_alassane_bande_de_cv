from django.urls import path
from .views import trombinoscope

urlpatterns = [
    path('', trombinoscope, name='accueil'),
]
