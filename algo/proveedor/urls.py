from django.conf.urls import patterns, include, url

urlpatterns = patterns('algo.proveedor.views',
	    url(r'^proveedor/$', 'proveedor', name='proveedor'),
	    url(r'^nuevoarticulo/$', 'nuevoarticulo', name='nuevoarticulo'),
	    url(r'^nuevatienda/$', 'nuevatienda', name='nuevatienda'),
	    url(r'^tiendas/$', 'tiendas', name='tiendas'),
) 