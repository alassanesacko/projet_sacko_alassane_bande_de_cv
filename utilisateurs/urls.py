from django.urls import path
from .views import inscription, connexion, deconnexion,profil

urlpatterns = [
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('profil/<int:user_id>/', profil, name='profil'),
]
