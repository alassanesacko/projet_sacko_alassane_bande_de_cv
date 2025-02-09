from django.db import models
from utilisateurs.models import Etudiant

class Trombinoscope(models.Model):
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE, related_name="trombinoscope")

    def __str__(self):
        return f"Trombinoscope: {self.etudiant.first_name} {self.etudiant.last_name}"
