from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object
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
    (r'^$', create_object, { 'model' : Arquivo, 'post_save_redirect' : '/arquivos/' }),
)
