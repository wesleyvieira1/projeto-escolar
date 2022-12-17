from django.contrib import admin

from usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = (
        'nome',
        'cpf',
        'rg',
        'endereco',
        'email',
        'endereco',
        'contato',
        'departamento',
        'senha',
        'confirm_senha',
        )
