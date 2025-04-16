from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    edad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.usuario.username

