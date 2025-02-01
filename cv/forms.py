from django import forms
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['titre', 'description','design']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

from django import forms
from .models import Experience, Formation, Competence, Langue, Projet

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['poste', 'entreprise', 'date_debut', 'date_fin', 'description']

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['diplome', 'etablissement', 'date_debut', 'date_fin']

class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ['libelle', 'niveau']

class LangueForm(forms.ModelForm):
    class Meta:
        model = Langue
        fields = ['libelle', 'niveau']

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'date_debut', 'date_fin']
