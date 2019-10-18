from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Turist
from django.views import generic

def index(request):
    return render(request, 'index.html', {})
	
def formulario(request):
    return render(request, 'mountain/formulario.html', {})

def galeria(request):
    return render(request, 'galeria.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})