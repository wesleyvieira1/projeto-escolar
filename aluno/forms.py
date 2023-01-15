from django import forms
from .models import Aluno
from turma.models import Turma
from .choices import *

class alunoForm(forms.ModelForm):
    turma_aluno = forms.ModelMultipleChoiceField(queryset=Turma.objects.all(),widget=forms.CheckboxSelectMultiple())
    turno_aluno = forms.ChoiceField(choices=choices_turno,widget=forms.Select(attrs={'class':'form-control'}))
    sexo_aluno = forms.ChoiceField(choices=choices_sexo,widget=forms.Select(attrs={'class':'form-control'}))
    raca_aluno = forms.ChoiceField(choices=choices_raca,widget=forms.Select(attrs={'class':'form-control'}))
    nome_aluno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o nome'}))
    cpf_aluno = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Digite o cpf'}))
    rg_aluno = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Digite o rg'}))
    email_aluno = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Digite o email'}))
    endereco_aluno  =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o endereço'}))
    contato_aluno = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Digite o contato'}))
    data_nascimento_aluno = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    data_entrada_aluno = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))


    class Meta:
        model = Aluno
        fields = ['nome_aluno','cpf_aluno',
        'rg_aluno','email_aluno',
        'endereco_aluno','contato_aluno',
        'turno_aluno','data_nascimento_aluno',
        'data_entrada_aluno','raca_aluno','sexo_aluno','turma_aluno'
        ]
