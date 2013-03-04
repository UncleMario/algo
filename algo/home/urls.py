from django.conf.urls import patterns, include, url

urlpatterns = patterns('algo.home.views',
	    url(r'^$', 'home', name='home'),
) 