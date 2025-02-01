from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Etudiant

class EtudiantCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    tel = forms.CharField(max_length=20, required=False)
    adresse = forms.CharField(widget=forms.Textarea, required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = Etudiant
        fields = ['username', 'email', 'tel', 'adresse', 'photo', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
