from django.db import models

# Create your models here.


class Contenidos(models.Model):
    nombre = models.CharField(max_length = 32)
    contenido = models.TextField()
