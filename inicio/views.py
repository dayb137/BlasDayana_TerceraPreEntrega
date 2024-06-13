from django.shortcuts import render, redirect
# from datetime import datetime
from inicio.models import Persona
from inicio.form import CrearPersonaFormulario,BuscarPersonas

def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_persona(request):
   
    if request.method == 'POST':
        formulario = CrearPersonaFormulario(request.POST)
        if formulario.is_valid():
         datos = formulario.cleaned_data
         persona = Persona(nommbre=datos.get('nombre'), apellido=datos.get('apellido'))
         persona.save()
         return redirect('inicio')
       
    
    return render(request,'inicio/crear.html', {'formulario':formulario})

def personas(request):
    return render(request, 'inicio/personas.html')