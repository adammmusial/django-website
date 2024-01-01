from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    # path("", views.contact, name=""),
    path("contact/", views.contact, name="contact_form")
]
