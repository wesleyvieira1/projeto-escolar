from django.shortcuts import render, redirect
from .models import Turma
from disciplina.models import Disciplina
from aluno.models import Aluno

def cadastroTurma(request):
    status = request.GET.get('status')
    dicipls = Disciplina.objects.all()
    alus = Aluno.objects.all() 
    return render(request, 'cadastro_turma.html', {'status':status, 'dicipls':dicipls,'alus':alus})

def validaCadastroTurma(request):
    ano_turma = request.POST.get('ano_turma')
    horario_inicio_turma = request.POST.get('hrI')
    horario_fim_turma = request.POST.get('hrF')
    etapa_turma = request.POST.get('etapa_turma')
    disciplina_turma = request.POST.get('disciplina_turma')
    dia_turma = request.POST.get('dia_turma')

    try:
        turma = Turma(
            ano_turma=ano_turma,
            horario_inicio_turma=horario_inicio_turma,
            horario_fim_turma=horario_fim_turma,
            etapa_turma=etapa_turma,
            disciplina_turma=disciplina_turma,
            dia_turma=dia_turma
        )
        turma.save()
        return redirect('/turma/cadastro/?status=0')
    except:
        return redirect('/turma/cadastro/?status=10')