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
    error_message = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid!")  # Debug
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                print("Sending email via Resend...")
                key = settings.RESEND_API_KEY
                if not key:
                    raise Exception("RESEND_API_KEY is not set.")
                
                # Sanitize the key: remove whitespace and 'Bearer ' if present
                key = key.strip()
                if key.lower().startswith("bearer "):
                    key = key[7:].strip()

                print(f"DEBUG: Using key starting with: {key[:5]}...")

                response = requests.post(
                    "https://api.resend.com/emails",
                    headers={"Authorization": f"Bearer {key}"},
                    json={
                        "from": "onboarding@resend.dev",
                        "to": [settings.CONTACT_RECIPIENT],
                        "subject": f"Portfolio Contact from {name}",
                        "text": f"From: {name} <{email}>\n\n{message}",
                    },
                    timeout=10
                )
                response.raise_for_status()
                sent = True
            except Exception as e:
                print(f"DEBUG: Full error: {e}")
                print("Resend error:", e)
                sent = False
                error_message = f"Failed to send email: {str(e)}"
    else:
        form = ContactForm()
    return render(request, "first_app/contact.html", {"form": form, "sent": sent, "error_message": error_message})