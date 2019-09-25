from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('formulario', views.formulario, name='formulario'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
]