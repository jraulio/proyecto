from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class CrearEstudiante(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)

class CrearProfesor(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    materia = forms.CharField(max_length=50)



