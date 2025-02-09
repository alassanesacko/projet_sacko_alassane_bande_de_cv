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
