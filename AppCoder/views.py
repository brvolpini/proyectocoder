from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse


# Create your views here.
def crea_curso(self,nombre,camada):

    curso = Curso(nombre=nombre, camada=camada)

    curso.save()
    
    return HttpResponse(f"Se creó el curso de {curso.nombre} con el numero de  camada {curso.camada}")