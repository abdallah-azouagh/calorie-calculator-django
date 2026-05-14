# calorie_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.calorie_form, name="calorie_form"),
]