from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required(login_url='/login/')
def home(request):
	return render_to_response('home/home.html',{},
		context_instance=RequestContext(request))