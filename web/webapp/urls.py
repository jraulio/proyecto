from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('', formulario, name="inicio"),
    path('lista-cursos/', listar_cursos, name="lista_cursos"),
    path('lista-estudiantes/', listar_estudiantes, name="lista_estudiantes"),
    path('lista-profesores/', listar_profesores, name="lista_profesores"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', crearEstudiante, name="estudiantes"),
    path('profesores/', crearProfesor, name="profesores"),
    path('curso-Formulario/', cursoFormulario, name="CursoFormulario"),
    ]
