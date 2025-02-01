from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.core.mail import EmailMessage
from io import BytesIO
from django.conf import settings
from weasyprint import HTML, CSS
from .models import CV
from .forms import CVForm
from .models import Experience, Formation, Competence, Langue, Projet
from .forms import ExperienceForm, FormationForm, CompetenceForm, LangueForm, ProjetForm

@login_required
def gerer_cv(request):
    etudiant = request.user
    cv, created = CV.objects.get_or_create(etudiant=etudiant)  # Récupérer ou créer un CV

    if request.method == "POST":
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Rediriger vers le dashboard après modification
    else:
        form = CVForm(instance=cv)

    return render(request, 'cv/gerer_cv.html', {'form': form})



# EXPÉRIENCE
@login_required
def ajouter_experience(request,cv_id):
    cv = get_object_or_404(CV, id=cv_id)  # Récupérer le CV correspondant

    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.cv = cv
            experience.save()
            return redirect('dashboard')
    else:
        form = ExperienceForm()
    return render(request, 'cv/ajouter_experience.html', {'form': form})


def modifier_experience(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)
    
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirection après modification
    else:
        form = ExperienceForm(instance=experience)

    return render(request, 'cv/modifier_langue.html', {'form': form})

@login_required
def supprimer_experience(request, id):
    experience = get_object_or_404(Experience, id=id,)
    experience.delete()
    return redirect('dashboard')

# FORMATION
@login_required
def ajouter_formation(request,cv_id):
    cv = get_object_or_404(CV, id=cv_id)  # Récupérer le CV correspondant

    if request.method == "POST":
        form = FormationForm(request.POST)
        if form.is_valid():
            formation = form.save(commit=False)
            formation.cv = cv
            formation.save()
            return redirect('dashboard')
    else:
        form = FormationForm()
    return render(request, 'cv/ajouter_formation.html', {'form': form})


def modifier_formation(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    
    if request.method == "POST":
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirection après modification
    else:
        form = FormationForm(instance=formation)

    return render(request, 'cv/modifier_langue.html', {'form': form})

@login_required
def supprimer_formation(request, id):
    formation = get_object_or_404(Formation, id=id)
    formation.delete()
    return redirect('dashboard')

# COMPÉTENCE
@login_required
def ajouter_competence(request,cv_id):
    cv = get_object_or_404(CV, id=cv_id)  # Récupérer le CV correspondant

    if request.method == "POST":
        form = CompetenceForm(request.POST)
        if form.is_valid():
            competence = form.save(commit=False)
            competence.cv = cv
            competence.save()
            return redirect('dashboard')
    else:
        form = CompetenceForm()
    return render(request, 'cv/ajouter_competence.html', {'form': form})


def modifier_competence(request, competence_id):
    competence = get_object_or_404(Competence, id=competence_id)
    
    if request.method == "POST":
        form = CompetenceForm(request.POST, instance=competence)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirection après modification
    else:
        form = CompetenceForm(instance=competence)

    return render(request, 'cv/modifier_langue.html', {'form': form})

@login_required
def supprimer_competence(request, id):
    competence = get_object_or_404(Competence, id=id,)
    competence.delete()
    return redirect('dashboard')

# LANGUE
@login_required

def ajouter_langue(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)  # Récupérer le CV correspondant

    if request.method == "POST":
        form = LangueForm(request.POST)
        if form.is_valid():
            langue = form.save(commit=False)
            langue.cv = cv  # Associer la langue au CV
            langue.save()
            return redirect('dashboard')  # Rediriger après ajout
    else:
        form = LangueForm()

    return render(request, 'cv/ajouter_langue.html', {'form': form, 'cv': cv})

def modifier_langue(request, langue_id):
    langue = get_object_or_404(Langue, id=langue_id)
    
    if request.method == "POST":
        form = LangueForm(request.POST, instance=langue)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirection après modification
    else:
        form = LangueForm(instance=langue)

    return render(request, 'cv/modifier_langue.html', {'form': form})

@login_required
def supprimer_langue(request, id):
    langue = get_object_or_404(Langue, id=id,)
    langue.delete()
    return redirect('dashboard')

# PROJET
@login_required
def ajouter_projet(request,cv_id):
    cv = get_object_or_404(CV, id=cv_id)  # Récupérer le CV correspondant

    if request.method == "POST":
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.cv = cv  # Associer la langue au CV
            projet.save()
            return redirect('dashboard')
    else:
        form = ProjetForm()
    return render(request, 'cv/ajouter_projet.html', {'form': form})

def modifier_projet(request, projet_id):
    projet = get_object_or_404(Langue, id=projet_id)
    
    if request.method == "POST":
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirection après modification
    else:
        form = ProjetForm(instance=projet)

    return render(request, 'cv/modifier_langue.html', {'form': form})

@login_required
def supprimer_projet(request, id):
    projet = get_object_or_404(Projet, id=id,)
    projet.delete()
    return redirect('dashboard')


#Generer le CV en pdf 




def generer_cv_pdf(request):
    etudiant = request.user
    cv = get_object_or_404(CV, etudiant=etudiant)

    # Charger le template HTML correct
    template_name = f"cv/cv_{cv.design}.html"
    template = get_template(template_name)

    context = {
        'etudiant': etudiant,
        'cv': cv,
        'experiences': cv.experience_set.all(),
        'formations': cv.formation_set.all(),
        'competences': cv.competence_set.all(),
        'langues': cv.langue_set.all(),
        'projets': cv.projet_set.all(),
    }

    html_string = template.render(context)

    # Récupérer le fichier CSS correspondant au design
    css_path = finders.find(f'cv/css/{cv.design}.css')
    css = CSS(filename=css_path) if css_path else None

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="CV_{etudiant.username}.pdf"'

    # Générer le PDF avec le CSS appliqué
    HTML(string=html_string).write_pdf(response, stylesheets=[css] if css else [])

    return response
#Envoi d'email



def envoyer_cv_email(request):
    if request.method == 'POST':
        destinataire = request.POST.get('email')
        etudiant = request.user
        cv = CV.objects.get(etudiant=etudiant)

        # Charger le bon template HTML
        template_name = f"cv/cv_{cv.design}.html"
        template = get_template(template_name)
        context = {
            'etudiant': etudiant,
            'cv': cv,
            'experiences': cv.experience_set.all(),
            'formations': cv.formation_set.all(),
            'competences': cv.competence_set.all(),
            'langues': cv.langue_set.all(),
            'projets': cv.projet_set.all(),
        }

        # Rendre le HTML
        html_string = template.render(context)

        # Récupérer le fichier CSS correspondant au design
        css_path = finders.find(f'cv/css/{cv.design}.css')
        css = CSS(filename=css_path) if css_path else None

        # Générer le PDF avec WeasyPrint
        pdf_buffer = BytesIO()
        HTML(string=html_string).write_pdf(pdf_buffer, stylesheets=[css] if css else [])
        pdf_buffer.seek(0)

        # Préparer l'email avec pièce jointe
        email = EmailMessage(
            subject="Votre CV en PDF",
            body="Bonjour,\n\nVous trouverez ci-joint votre CV généré automatiquement.\n\nCordialement.",
            from_email=settings.EMAIL_HOST_USER ,
            to=[destinataire]
        )
        email.attach(f"CV_{etudiant.username}.pdf", pdf_buffer.getvalue(), "application/pdf")

        try:
            email.send()
            return HttpResponse("CV envoyé avec succès !")
        except Exception as e:
            return HttpResponse(f"Erreur lors de l'envoi : {e}", status=500)
    return render(request, 'cv/envoyer_cv.html')
# Create your views here.
