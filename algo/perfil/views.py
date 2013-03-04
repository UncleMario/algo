from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from algo.perfil.forms import *
from algo.perfil.models import Perfil

@login_required(login_url='/login')
def perfil(request):
	currentUser=get_object_or_404(Perfil,user=request.user)
	if request.method == 'POST':
		form=PerfilForm(request.POST, instance=currentUser)
		if form.is_valid():
			perfil=form.save()
			return HttpResponse('Perfil guardado')
	else:
		form=PerfilForm(instance=currentUser)
	return render_to_response('perfil/perfil.html', {'form':form}, 
		context_instance=RequestContext(request))