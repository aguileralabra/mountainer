from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('formulario', views.formulario, name='formulario'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
]
