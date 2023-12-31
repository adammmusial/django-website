from django.url import path
from . import views

app_name = "contact"

urlpatterns = [
    path("",contact,name="")
]