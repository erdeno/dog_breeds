from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


class Dog(models.Model):
    name = models.CharField(max_length=64)
    link = models.CharField(max_length=64)
    smimg = models.CharField(max_length=64)
    bigimg = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        slug_name = slugify(unidecode(self.name))
        return f"dog/{self.id}/{slug_name}"

    def get_small_image(self):
        return f"/dogbreeds/images/dogs/dog_{self.id}_sm.jpg"

    def get_big_image(self):
        return f"/dogbreeds/images/dogs/dog_{self.id}_big.jpg"


class DogDetails(models.Model):
    class Meta:
        verbose_name_plural = "Dog Details"

    # dog = models.OneToOneField(Dog, on_delete=models.CASCADE)
    dog_id = models.IntegerField()
    dog_name = models.CharField(max_length=64)
    html_content = models.TextField()

    def __str__(self):
        return f"{self.dog_name} Özellikleri"
