from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import os
import resend
import requests
# Create your views here.


resend.api_key = os.environ.get("RESEND_API_KEY")


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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"Portfolio Contact from {name}",
            message=f"Message from {email}:\n\n{message}",
            from_email=None,
            recipient_list=["daud13t@gmail.com"],
            fail_silently=False,
        )

        return render(request, "first_app/contact.html", {"success": True})

    return render(request, "first_app/contact.html")
