from django import forms
from django.forms import ModelForm

from algo.proveedor.models import *


class ProveedorForm(ModelForm):
	class Meta:
		model=Proveedor

class ArticuloForm(ModelForm):
	class Meta:
		model=Articulo

class TiendaForm(ModelForm):
	class Meta:
		model=Tienda