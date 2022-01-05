from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField('nombre', max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    fecha_inscripcion = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechadeEntrega = models.DateField()
    entregado = models.BooleanField()