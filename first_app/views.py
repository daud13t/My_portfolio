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
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
             print("Form is valid!")  # Debug
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                  print("Sending email via Resend...")
                response = requests.post(
                    "https://api.resend.com/send",
                    headers={"Authorization": f"Bearer {settings.RESEND_API_KEY}"},
                    json={
                        "from": "daud13t@gmail.com",
                        "to": ["daud13t@gmail.com"],
                        "subject": f"Portfolio Contact from {name}",
                        "text": message,
                    },
                    timeout=10
                )
                response.raise_for_status()
                sent = True
            except Exception as e:
                print("Resend error:", e)
                sent = False
    else:
        form = ContactForm()
    return render(request, "first_app/contact.html", {"form": form, "sent": sent})