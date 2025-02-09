from django.urls import path
from . import views

urlpatterns = [
    path('creer/', views.creer_cv, name='creer_cv'),
    path('modifier/', views.modifier_cv, name='modifier_cv'),
    path('ajouter-experience/', views.ajouter_experience, name='ajouter_experience'),
    path('ajouter-formation/', views.ajouter_formation, name='ajouter_formation'),
    path('ajouter-langue/', views.ajouter_langue, name='ajouter_langue'),
    path('ajouter-competence/', views.ajouter_competence, name='ajouter_competence'),
]