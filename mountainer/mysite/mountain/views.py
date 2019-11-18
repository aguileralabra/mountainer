from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Turist, Imagen
from django.views import generic
from .forms import TuristCrear, ImagenCrear

def index(request):
    num_turist=Turist.objects.all().count()
    return render(request, 'index.html', context={'num_turist':num_turist},)
	

class TuristListView(generic.ListView):
    model = Turist
    paginate_by = 10

class TuristDetailView(generic.DetailView):
    model = Turist

def delete(request, turist_id):
    instancia = Turist.objects.get(id=turist_id)
    instancia.delete()

    return render(request,'deleterespuesta.html')


def crearTurist(request):
	if request.method =='POST':
		form = TuristCrear(request.POST)
		if form.is_valid():
			form.save()
		return render(request,'resultado.html')
	else:
		form = TuristCrear()

		return render(request,'FormularioTurist.html',{'form':form})

def resultado(request):
    return render(request,'resultado.html')


def edit(request, turist_id):
    instancia = Turist.objects.get(id=turist_id)
    form = TuristCrear(instance=instancia)
    if request.method == "POST":
        form = TuristCrear(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "edit.html", {'form': form})

def galeria(request):
    return render(request, 'galeria.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def index(request):
    num_imagen=Imagen.objects.all().count()
    return render(request, 'index.html', context={'num_imagen':num_imagen},)
	
class ImagenListView(generic.ListView):
    model = Imagen
    paginate_by = 10

class ImagenDetailView(generic.DetailView):
    model = Imagen

def crearImagen(request):
	if request.method =='POST':
		form = ImagenCrear(request.POST)
		if form.is_valid():
			form.save()
		return render(request,'resultadoimagen.html')
	else:
		form = ImagenCrear()

		return render(request,'Propuestas.html',{'form':form})

def resultadoimagen(request):
    return render(request,'resultadoimagen.html')

def editimagen(request, imagen_id):
    instancia = Imagen.objects.get(id=imagen_id)
    form = ImagenCrear(instance=instancia)
    if request.method == "POST":
        form = ImagenCrear(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "editimagen.html", {'form': form})

def deleteimagen(request, imagen_id):
    instancia = Imagen.objects.get(id=imagen_id)
    instancia.delete()

    return render(request,'resultadoeliminarimagen.html')