from django.urls import path
from . import views

urlpatterns = [
    path('cv/<int:cv_id>/pdf/', views.generer_pdf, name='generer_pdf'),

    path('creer/', views.creer_cv, name='creer_cv'),
    path('modifier/', views.modifier_cv, name='modifier_cv'),
    path('ajouter-experience/', views.ajouter_experience, name='ajouter_experience'),
    path('ajouter-formation/', views.ajouter_formation, name='ajouter_formation'),
    path('ajouter-langue/', views.ajouter_langue, name='ajouter_langue'),
    path('ajouter-competence/', views.ajouter_competence, name='ajouter_competence'),

    path('modifier_experience/<int:id>/', views.modifier_experience, name='modifier_experience'),
    path('supprimer_experience/<int:id>/', views.supprimer_experience, name='supprimer_experience'),

    path('modifier_formation/<int:id>/', views.modifier_formation, name='modifier_formation'),
    path('supprimer_formation/<int:id>/', views.supprimer_formation, name='supprimer_formation'),
    
    path('modifier_langue/<int:id>/', views.modifier_langue, name='modifier_langue'),
    path('supprimer_langue/<int:id>/', views.supprimer_langue, name='supprimer_langue'),
    
    path('modifier_competence/<int:id>/', views.modifier_competence, name='modifier_competence'),
    path('supprimer_competence/<int:id>/', views.supprimer_competence, name='supprimer_competence'),
]