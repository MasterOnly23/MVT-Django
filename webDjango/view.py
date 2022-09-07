from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso


def home(self, name):
    return HttpResponse(f'Pagina Home de {name}')

def page(self):
    lista = [1, 2, 3, 4]
    data = {'nombre': 'Pipe',
    'apellido': 'Daza',
    'lista': lista
    } #dentro del render para mandar variables a la pag
    planilla = loader.get_template('index.html') #loader viene a remplazar el open para cargar el template
    documento = planilla.render(data) #para renderizar el html
    return HttpResponse(documento)


def cursos(self):
    curso = Curso(nombre="HTML", camada="12045")
    curso.save()

    documento = f'Curso: {curso.nombre}\ncamada: {curso.camada}'
    return HttpResponse(documento)