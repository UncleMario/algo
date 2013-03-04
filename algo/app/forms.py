from django import forms
from django.forms import ModelForm

from algo.app.models import *


class CursoForm(ModelForm):
	class Meta:
		model=Curso

class CampusForm(ModelForm):
	class Meta:
		model=Campus

class AlumnoForm(ModelForm):
	class Meta:
		model=Alumno