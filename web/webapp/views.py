from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor
from .forms import CursoFormulario, CrearEstudiante, CrearProfesor

def curso(req, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f""" <p> Curso= {curso.nombre} - Camada = {curso.camada} creados con exito.</p>""")

def listar_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def listar_estudiantes(req):

    lista = Estudiante.objects.all()

    return render(req, "lista_estudiantes.html", {"lista_estudiantes": lista})

def listar_profesores(req):

    lista = Profesor.objects.all()

    return render(req, "lista_profesores.html", {"lista_profesores": lista})

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


def formulario(request):
    if request.method == 'POST':
        seleccion = request.POST.get('opcion_seleccionada')
        if seleccion == 'opcion1':
            return redirect('lista-cursos/')  
        elif seleccion == 'opcion2':
            return redirect('lista-estudiantes/') 
        elif seleccion == 'opcion3':
            return redirect('lista-profesores/')  

    return render(request, 'inicio.html')

    
