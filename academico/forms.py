from django import forms
from .models import Disciplina, Professor

class disciplinaForm(forms.ModelForm):
    nome_disciplina = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o nome da disciplina'}))
    professor_disciplina = forms.ModelChoiceField(queryset = Professor.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Disciplina
        fields = ['nome_disciplina','professor_disciplina']
