# grades/urls.py

from django.urls import path
from grades import views

urlpatterns = [
    path("", views.index, name="index"),
    path("grades/", views.index, name="index"),
    path("grades/predict", views.predict, name="predict"),
    path("grades/save", views.add, name="save"),
]
