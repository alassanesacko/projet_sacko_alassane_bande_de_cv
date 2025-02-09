
from django.contrib.auth.models import AbstractUser
from django.db import models

class Etudiant(AbstractUser):  # Chaque étudiant est un utilisateur
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
