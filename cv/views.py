from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CV, Experience, Formation, Langue, Competence, Projet
from .forms import CVForm, ExperienceForm, FormationForm, LangueForm, CompetenceForm, ProjetForm

@login_required
def creer_cv(request):
    cv, created = CV.objects.get_or_create(etudiant=request.user)
    form = CVForm(instance=cv)

    if request.method == 'POST':
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('modifier_cv')

    return render(request, 'cv/creer_cv.html', {'form': form})

@login_required
def modifier_cv(request):
    cv = get_object_or_404(CV, etudiant=request.user)
    experiences = Experience.objects.filter(cv=cv)
    formations = Formation.objects.filter(cv=cv)
    langues = Langue.objects.filter(cv=cv)
    competences = Competence.objects.filter(cv=cv)

    return render(request, 'cv/modifier_cv.html', {
        'cv': cv, 'experiences': experiences, 'formations': formations,
        'langues': langues, 'competences': competences
    })

@login_required
def ajouter_experience(request):
    cv = get_object_or_404(CV, etudiant=request.user)

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.cv = cv
            experience.save()
            return redirect('modifier_cv')

    else:
        form = ExperienceForm()

    return render(request, 'cv/ajouter_experience.html', {'form': form})
# Exemple pour modifier une expérience
from django.shortcuts import render, get_object_or_404, redirect
from .models import Experience
from .forms import ExperienceForm

@login_required
def modifier_experience(request, id):
    experience = get_object_or_404(Experience, id=id)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('profil', user_id=request.user.id)
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'cv/modifier_experience.html', {'form': form})

# Pour supprimer une expérience
@login_required
def supprimer_experience(request, id):
    experience = get_object_or_404(Experience, id=id)
    experience.delete()
    return redirect('profil', user_id=request.user.id)


@login_required
def ajouter_formation(request):
    cv = get_object_or_404(CV, etudiant=request.user)

    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            formation = form.save(commit=False)
            formation.cv = cv
            formation.save()
            return redirect('modifier_cv')

    else:
        form = FormationForm()

    return render(request, 'cv/ajouter_formation.html', {'form': form})

# Vues pour modifier une formation
@login_required
def modifier_formation(request, id):
    formation = get_object_or_404(Formation, id=id)
    if request.method == 'POST':
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            return redirect('profil',user_id=request.user.id)  # Redirection vers le profil de l'utilisateur
    else:
        form = FormationForm(instance=formation)
    return render(request, 'cv/modifier_formation.html', {'form': form})

# Vues pour supprimer une formation
@login_required
def supprimer_formation(request, id):
    formation = get_object_or_404(Formation, id=id)
    formation.delete()
    return redirect('profil',user_id=request.user.id)  # Redirection vers le profil de l'utilisateur



@login_required
def ajouter_langue(request):
    cv = get_object_or_404(CV, etudiant=request.user)

    if request.method == 'POST':
        form = LangueForm(request.POST)
        if form.is_valid():
            langue = form.save(commit=False)
            langue.cv = cv
            langue.save()
            return redirect('modifier_cv')

    else:
        form = LangueForm()

    return render(request, 'cv/ajouter_langue.html', {'form': form})

# Vues pour modifier une langue
@login_required
def modifier_langue(request, id):
    langue = get_object_or_404(Langue, id=id)
    if request.method == 'POST':
        form = LangueForm(request.POST, instance=langue)
        if form.is_valid():
            form.save()
            return redirect('profil',user_id=request.user.id)  # Redirection vers le profil de l'utilisateur
    else:
        form = LangueForm(instance=langue)
    return render(request, 'cv/modifier_langue.html', {'form': form})

# Vues pour supprimer une langue
@login_required
def supprimer_langue(request, id):
    langue = get_object_or_404(Langue, id=id)
    langue.delete()
    return redirect('profil',user_id=request.user.id)  # Redirection vers le profil de l'utilisateur



@login_required
def ajouter_competence(request):
    cv = get_object_or_404(CV, etudiant=request.user)

    if request.method == 'POST':
        form = CompetenceForm(request.POST)
        if form.is_valid():
            competence = form.save(commit=False)
            competence.cv = cv
            competence.save()
            return redirect('modifier_cv')

    else:
        form = CompetenceForm()

    return render(request, 'cv/ajouter_competence.html', {'form': form})
# Vues pour modifier une compétence
@login_required
def modifier_competence(request, id):
    competence = get_object_or_404(Competence, id=id)
    if request.method == 'POST':
        form = CompetenceForm(request.POST, instance=competence)
        if form.is_valid():
            form.save()
            return redirect('profil',user_id=request.user.id)  # Redirection vers le profil de l'utilisateur
    else:
        form = CompetenceForm(instance=competence)
    return render(request, 'cv/modifier_competence.html', {'form': form})

# Vues pour supprimer une compétence
@login_required
def supprimer_competence(request, id):
    competence = get_object_or_404(Competence, id=id)
    competence.delete()
    return redirect('profil',user_id=request.user.id)  # Redirection vers le profil de l'utilisateur
