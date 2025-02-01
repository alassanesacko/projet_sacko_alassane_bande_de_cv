from django.urls import path
from .views import inscription, connexion, deconnexion,dashboard

urlpatterns = [
    path('inscription/', inscription, name='inscription'),
    path('login/', connexion, name='login'),
    path('logout/', deconnexion, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),


]
