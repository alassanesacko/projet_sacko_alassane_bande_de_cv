from django.shortcuts import render, redirect, get_object_or_404
from cv.models import CV
from datetime import datetime
from django.contrib import messages
from .utils import send_email_with_html_body

# Create your views here.



def envoi_mail(request,cv_id, ):
    """ This view help to create and account for testing sending mails."""
    if request.method == "POST":
        cv = get_object_or_404(CV, id=cv_id, etudiant=request.user)
        email = request.POST.get('email')

        subjet = "ENVOI DE CV PAR MAIL"
        template = 'cv/cv_pdf.html'
        context = {
            'date': datetime.today().date,
            'email': email,
            'cv':cv
        }

        receivers = [email]

        has_send = send_email_with_html_body(
            subjet=subjet,
            receivers=receivers,
            template=template,
            context=context
            )

        if has_send:
            messages.success(request, "Mail envoyé avec succès.")
        else:
            messages.error(request, "Erreur lors de l'envoi de l'email.")
    return render(request,'cv/email.html' )       