from django import forms
from academico.models import Disciplina
from .models import Turma
from .choices import *

class turmaForm(forms.ModelForm):
    ano_turma = forms.ChoiceField(choices=choices_ano,widget=forms.Select(attrs={'class':'form-control'}))
    horario_inicio_turma = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type':'time'}))
    horario_fim_turma = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type':'time'}))
    etapa_turma = forms.ChoiceField(choices=choices_etapa,widget=forms.Select(attrs={'class':'form-control'}))
    disciplina_turma = forms.ModelChoiceField(queryset=Disciplina.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    dia_turma = forms.ChoiceField(choices=choices_dia, initial='---------',widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Turma
        fields = ['ano_turma','horario_inicio_turma','horario_fim_turma','etapa_turma','disciplina_turma','dia_turma']





    '''nome_disciplina = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o nome da disciplina'}))
    professor_disciplina = forms.ModelChoiceField(queryset = Professor.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))'''