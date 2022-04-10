from django.db import models

# Create your models here.
class Usuario(models.Model): # Tabla Usuario
    nombre = models.CharField(null=False, blank=False, max_length=250)
    apellido = models.CharField(null=False, blank=False, max_length=250)
    email = models.CharField(null=False, blank=False, max_length=250)