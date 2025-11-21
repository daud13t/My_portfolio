from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.

class Home(generic.TemplateView):
      template_name = 'first_app/home.html'
      
class about(generic.TemplateView):
      template_name="first_app/about.html"

class project1(generic.TemplateView):
      template_name = "project1/BOOTSTRAP_Project.html"

class project2(generic.TemplateView):
      template_name = "project2/h.html"

class sign_in_for_project1(generic.TemplateView):
      template_name = "project1/sign_in.html"



def contact_view(request):
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

          
            send_mail(
                subject=f"Portfolio Contact from {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["daud13t@gmail.com"], 
                fail_silently=False,
            )

            sent = True
    else:
        form = ContactForm()

    return render(request, "first_app/contact.html", {"form": form, "sent": sent})