from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Estudiante, Profesor
from .forms import CursoFormulario, CrearEstudiante, CrearProfesor

def curso(req, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f""" <p> Curso= {curso.nombre} - Camada = {curso.camada} creados con exito.</p>""")

def listar_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def inicio(req):

    return render(req, "inicio.html")

def cursos(req):
    
    return render(req, "cursos.html")

def profesores(req):
    
    return render(req, "profesores.html")

def estudiantes(req):
    
    return render(req, "estudiantes.html")

def entregables(req):
    
    return render(req, "entregables.html")

def cursoFormulario(req):

    print('method', req.method)
    print('POST', req.POST)


    if req.method == 'POST':

        miFormulario = CursoFormulario(req.POST)
    
        if miFormulario.is_valid():
           
           data = miFormulario.cleaned_data
           curso = Curso(nombre=data["curso"], camada=data["camada"])
           curso.save()
           return render(req, "inicio.html")
    
    else:
        miFormulario = CursoFormulario()
        return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})
    

def crearEstudiante(req):

    print('method', req.method)
    print('POST', req.POST)


    if req.method == 'POST':

        miFormulario = CrearEstudiante(req.POST)
    
        if miFormulario.is_valid():
           
           data = miFormulario.cleaned_data
           curso = Estudiante(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], contraseña=data["contraseña"],)
           curso.save()
           return render(req, "inicio.html")
    
    else:
        miFormulario = CrearEstudiante()
        return render(req, "estudiantes.html", {"miFormulario": miFormulario})
    
def crearProfesor(req):

    print('method', req.method)
    print('POST', req.POST)


    if req.method == 'POST':

        miFormulario = CrearProfesor(req.POST)
    
        if miFormulario.is_valid():
           
           data = miFormulario.cleaned_data
           curso = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], materia=data["materia"],)
           curso.save()
           return render(req, "inicio.html")
    
    else:
        miFormulario = CrearProfesor()
        return render(req, "profesores.html", {"miFormulario": miFormulario})
    

def busqueda(req):
    return render(req, "inicio.html")


    
def buscar(req):
    busqueda = req.GET('busqueda', '')
    tipo_busqueda = req.GET('tipo_busqueda', '')

    resultados = []

    if tipo_busqueda == 'usuario':
        resultados = Estudiante.objects.filter(nombre__icontains=busqueda)
    elif tipo_busqueda == 'curso':
        resultados = Curso.objects.filter(nombre__icontains=busqueda)
    elif tipo_busqueda == 'profesor':
        resultados = Profesor.objects.filter(nombre__icontains=busqueda)

    return render(req, 'resultados_busquedas.html', {'resultados': resultados, 'busqueda': busqueda, 'tipo_busqueda': tipo_busqueda})