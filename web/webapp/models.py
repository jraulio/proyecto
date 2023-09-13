from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
    class Meta():
        verbose_name = 'Course'
        verbose_name_plural = 'The Courses'

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}- {self.apellido}'

class Profesor (models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    materia = models.CharField(max_length=50)