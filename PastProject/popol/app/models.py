from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Popol(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.CharField( max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)