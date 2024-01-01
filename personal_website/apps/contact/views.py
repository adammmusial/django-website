from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from personal_website import settings
import bleach


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ContactForm()

    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.cleaned_data["name"]
            email = bleach.cleaned_data["email"]
            message = bleach.cleaned_data["message"]
            send_mail(f"{name} sent an email", message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, "contact.html", {"form": form, "success": True}) 
    else: 
        raise NotImplementedError
    
    return render(request, "contact.html", {"form": form})

# def contact_form(request: HttpRequest) -> HttpResponse:
#     return render(request, 'contact.html')  # Return the rendered response
