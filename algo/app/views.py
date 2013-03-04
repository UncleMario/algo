from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext


from algo.app.forms import *

def nuevoalumno(request):
	if request.method == 'POST':
		form=AlumnoForm(request.POST)
		if form.is_valid():
			nuevoalumno=form.save()
			return HttpResponse('Formulario guardado correctamente!!!')
	else:
		form=AlumnoForm()
	return render_to_response('app/nuevoalumno.html',{'form':form},
		context_instance=RequestContext(request))

def nuevocurso(request):
	if request.method == 'POST':
		form=CursoForm(request.POST)
		if form.is_valid():
			nuevocurso=form.save()
			return HttpResponse('Formulario guardado correctamente!!!')
	else:
		form=CursoForm()
	return render_to_response('app/nuevocurso.html',{'form':form},
		context_instance=RequestContext(request))

def nuevocampus(request):
	if request.method == 'POST':
		form=CampusForm(request.POST)
		if form.is_valid():
			nuevocampus=form.save()
			return HttpResponse('Formulario guardado correctamente!!!')
	else:
		form=CampusForm()
	return render_to_response('app/nuevocampus.html',{'form':form},
		context_instance=RequestContext(request))
