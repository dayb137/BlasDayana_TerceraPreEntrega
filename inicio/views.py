from django.shortcuts import render, redirect
from inicio.models import Persona
from inicio.form import CrearPersonaFormulario, BuscarPersona


def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_persona(request):
    
    formulario = CrearPersonaFormulario()
   
    if request.method == 'POST':
        formulario = CrearPersonaFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            persona = Persona(nommbre=datos.get('nombre'), apellido=datos.get('apellido'))
            persona.save()   
            return redirect('personas')
    
                    
    return render(request,'inicio/crear_persona.html', {'formulario':formulario})
       
    
def personas(request):
    
    formulario = BuscarPersona(request.GET)
    
    if formulario.is_valid():
        apellido = formulario.cleaned_data['apellido']
        personas = Persona.objects.filter(apellido__icontains=apellido)
    
    
    return render(request, 'inicio/personas.html', {'personas':personas , 'formulario': formulario})