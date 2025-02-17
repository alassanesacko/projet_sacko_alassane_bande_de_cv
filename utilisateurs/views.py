from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Etudiant

from cv.models import CV  # Import du modèle CV

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Création automatique du CV après l'inscription
            CV.objects.create(etudiant=request.user, titre="Mon CV", description="CV généré automatiquement")
            messages.success(request, "Inscription réussie ! Votre CV a été créé.")
            return redirect('profil', user_id=user.id)
    else:
        form = CustomUserCreationForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Vérifier si l'utilisateur a un CV, sinon en créer un
            if not CV.objects.filter(etudiant=request.user).exists():
                CV.objects.create(etudiant=request.user, titre="Mon CV", description="CV généré automatiquement")
            return redirect('profil', user_id=user.id)
    else:
        form = AuthenticationForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})


def deconnexion(request):
    logout(request)
    return redirect('connexion')



@login_required
def profil(request, user_id):
    etudiant = get_object_or_404(Etudiant, id=user_id)
    
    # Vérifier si un CV existe pour cet étudiant, sinon le créer
    cv, created = CV.objects.get_or_create(etudiant=etudiant, defaults={
        'titre': "Mon CV",
        'description': "CV généré automatiquement"
    })

    return render(request, 'utilisateurs/profil.html', {'etudiant': etudiant, 'cv': cv})

