from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('', busqueda, name="inicio"),
    path('lista-cursos/', listar_cursos, name="lista_cursos"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', crearEstudiante, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('profesores/', crearProfesor, name="profesores"),
    path('curso-Formulario/', cursoFormulario, name="CursoFormulario"),
    path('busqueda-camada/', busqueda, name="busqueda_camada"),
    path('buscar/', buscar, name="resultados_busquedas"),
    path('resultado/', buscar, name='resultado_busquedas'),
    ]
