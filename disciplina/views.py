from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Disciplina, Professor
from .forms import disciplinaForm


def cadastroDisciplina(request):
    status = request.GET.get('status')
    form = disciplinaForm()
    return render(request, 'cadastro_disciplina.html', {'form':form, 'status':status})


def validaCadastroDisciplina(request):
    nome_disciplina = request.POST.get('nome_disciplina')
    professor_disciplina = request.POST.get('professor_disciplina')
    
    disciplina = Disciplina(nome_disciplina=nome_disciplina, professor_disciplina=professor_disciplina)
    disciplina.save()
    '''try:
        disciplina = Disciplina(nome_disciplina=nome_disciplina, professor_disciplina=professor_disciplina)
        disciplina.save()
        return redirect('/disciplina/cadastro/?status=0')
    except:
        return redirect('/disciplina/cadastro/?status=10')'''



