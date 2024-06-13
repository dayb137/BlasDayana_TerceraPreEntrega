from django.shortcuts import render
from datetime import datetime

from inicio.models import Persona


def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_persona(request, nombre, apellido):
    persona = Persona(nombre=nombre, apellido=apellido)
    persona.save()
    return render(request,'persona_templates/crear.html',{'persona':persona})

