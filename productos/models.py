from ctypes import create_unicode_buffer
from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import commondialog
from turtle import mode
from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion=models.CharField(max_length=50, verbose_name='Descripción')
    codigo=models.CharField(max_length=20, verbose_name='Código', help_text="Ingrese el código del producto")
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='productos')
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    def __str__(self):
        return self.descripcion
