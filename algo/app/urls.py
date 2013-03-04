from django.conf.urls import patterns, include, url

urlpatterns = patterns('algo.app.views',
	    url(r'^nuevoalumno/$', 'nuevoalumno', name='nuevoalumno'),
	    url(r'^nuevocurso/$', 'nuevocurso', name='nuevocurso'),
	    url(r'^nuevocampus/$', 'nuevocampus', name='nuevocampus'),
) 