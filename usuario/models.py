from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=7)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    contato = models.CharField(max_length=11)
    departamento = models.CharField(max_length=50)
    senha = models.CharField(max_length=8)
    confirm_senha = models.CharField(max_length=8)
    img_user = models.ImageField(upload_to='usuario_profile', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

class Users(AbstractUser):
    rg_user = models.CharField(max_length=7)
    cpf_user = models.CharField(max_length=11)
    contato_user = models.CharField(max_length=11)
    departamento_user = models.CharField(max_length=50)
    img_user = models.ImageField(upload_to='user_profile', null=True, blank=True)