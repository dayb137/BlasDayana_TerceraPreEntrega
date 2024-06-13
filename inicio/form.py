from django import forms

class CrearPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    
class BuscarPersonas(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)