from django.conf.urls import patterns, include, url

urlpatterns = patterns('algo.perfil.views',
	    url(r'^perfil/$', 'perfil', name='perfil'),
) 