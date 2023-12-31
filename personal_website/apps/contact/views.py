from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def contact(request: HttpRequest) -> HttpRequest:
    return render(request, "contact.html")
