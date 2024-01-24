from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="index" ),
    path("<int:month>", views.monthly_challanges_in_number),
    path("<str:month>", views.monthly_challange, name="monthly_challange")
]