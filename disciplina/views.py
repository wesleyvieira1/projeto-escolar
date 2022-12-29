from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Disciplina, Professor


def cadastroDisciplina(request):
    status = request.GET.get('status')
    profs = Professor.objects.all()
    return render(request, 'cadastro_disciplina.html', {'profs':profs, 'status':status})


def validaCadastroDisciplina(request):
    nome_disciplina = request.POST.get('nome_disciplina')
    nome_professor = request.POST.get('nome_disciplina_professor')
    

    try:
        disciplina = Disciplina(nome_disciplina=nome_disciplina,professor_disciplina=nome_professor)
        disciplina.save()
        return redirect('/disciplina/cadastro/?status=0')
    except:
        return redirect('/disciplina/cadastro/?status=10')



