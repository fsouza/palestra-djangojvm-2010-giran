from django.conf.urls.defaults import *
from django.conf import settings
from core.models import Arquivo

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^lentoxer/', include('lentoxer.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.criar_arquivo', name = 'novo_arquivo'),
    url(r'^arquivos', 'django.views.generic.list_detail.object_list', { 'queryset' : Arquivo.objects.all() }, name = 'listar_arquivos'),
    (r'^media/(.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
)
