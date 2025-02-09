from django import forms
from .models import CV, Experience, Formation, Langue, Competence, Projet

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['titre', 'description']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['poste', 'entreprise', 'date_debut', 'date_fin', 'description']
        widgets = {
            'poste': forms.TextInput(attrs={'class': 'form-control'}),
            'entreprise': forms.TextInput(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['diplome', 'etablissement', 'date_debut', 'date_fin']
        widgets={
            'diplome': forms.TextInput(attrs={'class': 'form-control'}),
            'etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})

        }

class LangueForm(forms.ModelForm):
    class Meta:
        model = Langue
        fields = ['libelle', 'niveau']
        widgets={
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau': forms.TextInput(attrs={'class': 'form-control'}),
        }
class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ['libelle', 'niveau']
        widgets={
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'date_debut', 'date_fin']
        widgets={
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'descrition': forms.Textarea(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})

        }
