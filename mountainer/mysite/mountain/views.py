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


def editarTurist(request):
    if request.method == "POST":
        form = TuristCrear(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
    else:
        form = TuristCrear()
    return render(request, 'editar.html', {'form': form})

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

def hecho(request):
    return render(request,'hecho.html')


def editarImagen(request):
    if request.method == "POST":
        form = ImagenCrear(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
    else:
        form = ImagenCrear()
    return render(request, 'editar.html', {'form': form})