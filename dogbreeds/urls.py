from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.DogList.as_view(), name="index"),
    path("dog/<int:dogid>/<slug:slug>", views.dog, name="dog"),
]
