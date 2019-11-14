from django import forms
from .models import Turist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TuristCrear(forms.ModelForm):
	Nombre = forms.CharField(widget=forms.TextInput(

		attrs={
			'class': 'form-control',
			'placeholder': 'Escriba su Nombre'
		}
	))
	Apellido = forms.CharField(widget=forms.TextInput(

		attrs={
			'class': 'form-control',
			'placeholder': 'Escriba su Apellido'
		}
	))
	telefono = forms.IntegerField(widget=forms.TextInput(

		attrs={
			'class': 'form-control',
			'placeholder': 'Escriba su numero Telefonico'
		}
	))
	pais = forms.CharField(widget=forms.TextInput(

		attrs={
			'class': 'form-control',
			'placeholder': 'Pais en el que vive'
		}
	))	
	lugar = forms.CharField(widget=forms.TextInput(

		attrs={
			'class': 'form-control',
			'placeholder': 'Escriba el lugar deseado de ir'
		}
	))	
	Opinion = forms.CharField(widget=forms.TextInput(

		attrs={
			'class': 'form-control',
			'placeholder': 'Escriba su opinion',
			'cols': 20
		}
	))
	class Meta:
		model = Turist

		fields = [
			'Nombre',
			'Apellido',
			'telefono',
			'pais',
			'lugar',
			'Opinion',
		]