from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import EtudiantCreationForm, LoginForm

from django.contrib.auth.decorators import login_required
from cv.models import *


@login_required
def dashboard(request):
    etudiant = request.user
    cv = CV.objects.filter(etudiant=etudiant).first()  # Récupérer le CV de l'étudiant
    context={
        'etudiant': etudiant,
        'cv': cv,
        'langue':Langue,
        'experience':Experience,
        'projet':Projet,
        'competence':Competence,
        'formation':Formation,
    }
    return render(request, 'utilisateurs/dashboard.html', context=context)


def inscription(request):
    if request.method == "POST":
        form = EtudiantCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = EtudiantCreationForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})

def connexion(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('login')

# Create your views here.
