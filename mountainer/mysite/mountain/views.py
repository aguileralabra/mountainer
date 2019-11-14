from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Turist
from django.views import generic
from .forms import TuristCrear

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

def hecho(request):
    return render(request,'hecho.html')


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