from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from algo.proveedor.forms import *
from algo.proveedor.models import *

@login_required(login_url='/login')
def proveedor(request):
	currentUser=get_object_or_404(Proveedor,user=request.user)
	if request.method == 'POST':
		form=ProveedorForm(request.POST, instance=currentUser)
		if form.is_valid():
			proveedor=form.save()
			return HttpResponse('Perfil guardado')
	else:
		form=ProveedorForm(instance=currentUser)
	return render_to_response('proveedor/proveedor.html', {'form':form}, 
		context_instance=RequestContext(request))

def nuevoarticulo(request):
	if request.method == 'POST':
		form=ArticuloForm(request.POST)
		if form.is_valid():
			nuevoarticulo=form.save()
			return HttpResponse('Formulario guardado correctamente!!!')
	else:
		form=ArticuloForm()
	return render_to_response('proveedor/nuevoarticulo.html',{'form':form},
		context_instance=RequestContext(request))

def nuevatienda(request):
	if request.method == 'POST':
		form=TiendaForm(request.POST)
		if form.is_valid():
			nuevatienda=form.save()
			return HttpResponse('Formulario guardado correctamente!!!')
	else:
		form=TiendaForm()
	return render_to_response('proveedor/nuevatienda.html',{'form':form},
		context_instance=RequestContext(request))

def tiendas(request):
	tiendas=Tienda.objects.all()
	return render_to_response('proveedor/tiendas.html',{'tiendas':tiendas},
		context_instance=RequestContext(request))