from django.shortcuts import render, redirect
# from datetime import datetime
from inicio.models import Persona
from inicio.form import CrearPersonaFormulario

def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_persona(request):
   
    if request.method == 'POST':
        formulario = CrearPersonaFormulario(request.POST)
        if formulario.is_valid():
         datos = formulario.cleaned_data
         persona = Persona(nommbre=datos.get('nombre'), apellido=datos.get('apellido'))
         persona.save()
         return redirect('personas')
        else:
            formulario = CrearPersonaFormulario()
    return render(request,'inicio/crear.html', {'formulario':formulario})
       
    

def personas(request):
    persona = Persona.objects.all()
    return render(request, 'inicio/personas.html')