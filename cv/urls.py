from django.urls import path
from .views import gerer_cv
from .views import *

urlpatterns = [
    path('gerer/', gerer_cv, name='gerer_cv'),

    path('experience/ajouter/<int:cv_id>', ajouter_experience, name='ajouter_experience'),
    path('experience/supprimer/<int:id>/', supprimer_experience, name='supprimer_experience'),
    path('experience/modifier/<int:experience_id>/', modifier_experience, name='modifier_experience'),

    path('formation-ajouter/<int:cv_id>', ajouter_formation, name='ajouter_formation'),
    path('formation/supprimer/<int:id>/', supprimer_formation, name='supprimer_formation'),
    path('formation/modifier/<int:formation_id>/', modifier_formation, name='modifier_formation'),

    path('competence-ajouter/<int:cv_id>', ajouter_competence, name='ajouter_competence'),
    path('competence/supprimer/<int:id>/', supprimer_competence, name='supprimer_competence'),
    path('competence/modifier/<int:competence_id>/', modifier_competence, name='modifier_competence'),

    path('ajouter-langue/<int:cv_id>/', ajouter_langue, name='ajouter_langue'),
    path('langue/supprimer/<int:id>/', supprimer_langue, name='supprimer_langue'),
    path('langue/modifier/<int:langue_id>/', modifier_langue, name='modifier_langue'),


    path('projet-ajouter/<int:cv_id>', ajouter_projet, name='ajouter_projet'),
    path('projet/supprimer/<int:id>/', supprimer_projet, name='supprimer_projet'),
    path('projet/modifier/<int:projet_id>/', modifier_projet, name='modifier_projet'),
    path('generer_pdf/', generer_cv_pdf, name='generer_cv_pdf'),

    path('envoyer-cv/', envoyer_cv_email, name='envoyer_cv_email'),
]

