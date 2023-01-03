from django import forms
from .models import Disciplina

class disciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['professor_disciplina']
