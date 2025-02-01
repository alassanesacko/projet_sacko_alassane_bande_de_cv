from django.db import models

""" from django.contrib.auth.models import User
 """
from django.conf import settings
User = settings.AUTH_USER_MODEL


""" class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=20)
    adresse = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}" """

class CV(models.Model):
    DESIGN_CHOICES = [
        ('design1', 'Modèle Classique'),
        ('design2', 'Modèle Moderne'),
        ('design3', 'Modèle Créatif') ]
    
    etudiant = models.OneToOneField(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    design = models.CharField(max_length=20, choices=DESIGN_CHOICES, default='design1')


    def __str__(self):
        return self.titre

class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    poste = models.CharField(max_length=200)
    entreprise = models.CharField(max_length=200)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

class Formation(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    diplome = models.CharField(max_length=200)
    etablissement = models.CharField(max_length=200)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

class Langue(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)

class Competence(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)

class Projet(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

# Create your models here.
