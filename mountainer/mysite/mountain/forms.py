from django import forms
from .models import Turist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TuristCrear(forms.ModelForm):

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