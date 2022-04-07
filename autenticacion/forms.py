from cProfile import label
import email
from django import forms
class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.EmailField(label="Correo",required=True)
    telefono=forms.CharField(label="Telefono",required=True)
    contenido=forms.CharField(label="Requerimiento", widget=forms.Textarea, required=True)

