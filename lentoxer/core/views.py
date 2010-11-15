# Create your views here.
from django.views.generic.create_update import create_object
from django.core.urlresolvers import reverse
from core.models import Arquivo

def criar_arquivo(request):
    return create_object(request, model=Arquivo, post_save_redirect=reverse('listar_arquivos'))
