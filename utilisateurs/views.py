from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import EtudiantCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cv.models import *
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Etudiant # Import des modèles

def trombinoscope(request):
    etudiants = Etudiant.objects.all().select_related('cv')  # Charge les étudiants avec leur CV
    paginator = Paginator(etudiants, 6)  # Afficher 6 étudiants par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'utilisateurs/trombinoscope.html', {'page_obj': page_obj})





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
            messages.success(request, "Inscription réussie ! 🎉 Bienvenue sur la plateforme.")
            return redirect('dashboard')
        else:
            messages.error(request, "Une erreur est survenue lors de l'inscription. Vérifiez les informations saisies.")

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
            messages.warning(request, "Identifiant ou mot de passe incorrect ! ❌")
    else:
        form = LoginForm()

    return render(request, 'utilisateurs/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('login')

# Create your views here.
