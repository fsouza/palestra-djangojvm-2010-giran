from django.db import models

# Create your models here.
class Arquivo(models.Model):
    arquivo = models.FileField(upload_to="arquivos", max_length=100)
