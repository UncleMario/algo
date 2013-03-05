from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login,logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'algo.views.home', name='home'),
    # url(r'^algo/', include('algo.foo.urls')),
    url(r'^app/', include('algo.app.urls')),
    url(r'^perfil/', include('algo.perfil.urls')),
    url(r'^proveedor/', include('algo.proveedor.urls')),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^', include('algo.home.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
