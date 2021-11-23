from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Dog, DogDetails

import random


class DogList(ListView):
    model = Dog
    template_name = "dogbreeds/index.html"
    paginate_by = 12


def dog(request, dogid, slug):
    dog = Dog.objects.get(pk=int(dogid))
    dogDetails = DogDetails.objects.get(dog_id=int(dogid))

    return render(request, "dogbreeds/dog.html", {"dog": dog, "dogDetails": dogDetails})
