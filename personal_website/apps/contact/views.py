from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import ContactForm


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ContactForm()
        return render(
            request, "contact.html", {"form": form}
        )  # Return the rendered response
    else:
        raise NotImplementedError


# def contact_form(request: HttpRequest) -> HttpResponse:
#     return render(request, 'contact.html')  # Return the rendered response
