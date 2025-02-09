from django.shortcuts import render
from utilisateurs.models import Etudiant
from django.core.paginator import Paginator

def trombinoscope(request):
    # Récupérer tous les étudiants
    etudiants = Etudiant.objects.all()

    # Pagination : 6 étudiants par page
    paginator = Paginator(etudiants, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'trombinoscope/trombinoscope.html', {'page_obj': page_obj,})
