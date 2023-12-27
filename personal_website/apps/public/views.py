from django.shortcuts import render 

def index(request: HttpRequest) -> HttpRequest:
    print(request.user)
    return render(request,'index.html')

def about(request HttpRequest) -> HttpRequest:
    return render(request,'about.html')

def contact(request HttpRequest) -> HttpRequest:
    return render(request,'contact.html')
