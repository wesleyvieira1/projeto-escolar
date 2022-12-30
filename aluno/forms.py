from django import forms
from .models import Aluno

class alunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_aluno','cpf_aluno',
        'rg_aluno','email_aluno',
        'endereco_aluno','contato_aluno',
        'turno_aluno','data_nascimento_aluno',
        'data_entrada_aluno','raca_aluno','sexo_aluno'
        ]

        widgets = {
            'nome_aluno':forms.TextInput(attrs={'class':'form-control'}),
            'cpf_aluno':forms.TextInput(attrs={'class':'form-control'}),
            'rg_aluno':forms.TextInput(attrs={'class':'form-control'}),
            'email_aluno':forms.TextInput(attrs={'class':'form-control'}),
            'endereco_aluno':forms.TextInput(attrs={'class':'form-control'}),
            'contato_aluno':forms.TextInput(attrs={'class':'form-control'}),
            'turno_aluno':forms.TextInput(attrs={'class':'form-control'}),
            'data_nascimento_aluno':forms.DateInput(attrs={'class':'form-control'}),
            'data_entrada_aluno':forms.DateInput(attrs={'class':'form-control'}),
            'raca_aluno':forms.TextInput(attrs={'class':'form-control'}),
            'sexo_aluno':forms.TextInput(attrs={'class':'form-control'}),
        }   
