from django.db import models
from utilisateurs.models import Etudiant

class CV(models.Model):
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE, related_name="cv")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"CV de {self.etudiant.first_name} {self.etudiant.last_name}"

class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="experiences")
    poste = models.CharField(max_length=255)
    entreprise = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.poste} chez {self.entreprise}"

class Formation(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="formations")
    diplome = models.CharField(max_length=255)
    etablissement = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.diplome} à {self.etablissement}"

class Langue(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="langues")
    libelle = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.libelle} ({self.niveau})"

class Competence(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="competences")
    libelle = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.libelle} ({self.niveau})"

class Projet(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="projets")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titre
