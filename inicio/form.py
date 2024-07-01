from django import forms

class CrearPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    
class BuscarPersona(forms.Form):
    apellido = forms.CharField(max_length=30, required=False)
