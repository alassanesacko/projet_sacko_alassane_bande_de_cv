from django.contrib.auth.models import AbstractUser
from django.db import models

class Etudiant(AbstractUser):  
    tel = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.email})"

# Create your models here.
