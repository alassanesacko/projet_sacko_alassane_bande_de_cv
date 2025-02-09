from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Etudiant

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control'}))
    adresse = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    class Meta:
        model = Etudiant
        fields = ['username','first_name', 'last_name', 'email', 'tel', 'adresse','photo', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
