from django.db import models
from django.db.models.base import Model

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="Uploads/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Aboutpage(models.Model):
    profilepic = models.ImageField(upload_to="Uploads/")
