from django import forms
from django.forms import ModelForm

from algo.perfil.models import *


class PerfilForm(ModelForm):
	class Meta:
		model=Perfil
		exclude=('user','friends',)