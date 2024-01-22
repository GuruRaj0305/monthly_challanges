from django.urls import path
from . import views


urlpatterns = [
    path("challanges",views.index )
]