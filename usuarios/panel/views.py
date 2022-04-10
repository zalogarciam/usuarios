from django.shortcuts import redirect, render
from django.urls import reverse
from panel.models import Usuario
# Create your views here.

# INSERT SQL
def home(request):
    if request.POST:
        usuario = Usuario(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            email = request.POST['email']
        )
        usuario.save()
    return render(request, 'panel/home.html', locals())

# SELECT 
def list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'panel/list.html', locals())

# UPDATE

def edit(request, pk):
    usuario = Usuario.objects.get(pk = pk)
   
    if request.POST:
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.email = request.POST['email']
        usuario.save()
    return render(request, 'panel/home.html', locals())
  
# DELETE

def delete(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    usuario.delete()
    return redirect(reverse('panel:list'))
