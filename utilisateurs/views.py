from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Etudiant

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie !")
            return redirect('profil',user_id=user.id)
    else:
        form = CustomUserCreationForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profil',user_id=user.id)
    else:
        form = AuthenticationForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('connexion')


@login_required
def profil(request, user_id):
    etudiant = get_object_or_404(Etudiant, id=user_id)
    return render(request, 'utilisateurs/profil.html', {'etudiant': etudiant})
