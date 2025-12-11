from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        "placeholder": "Your name", "class": "form-control"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Your email", "class": "form-control"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Write your message...", "rows": 5, "class": "form-control"
    }))
