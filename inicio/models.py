from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
 
    def __str__(self):
     return f'Soy  {self.nombre} {self.apellido}'
