from django.contrib import admin

from .models import Dog, DogDetails

admin.site.register(Dog)
admin.site.register(DogDetails)
