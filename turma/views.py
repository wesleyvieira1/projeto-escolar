from django.shortcuts import render, redirect
from .models import Turma
from academico.models import Disciplina
from aluno.models import Aluno
from .forms import turmaForm
from django.views.generic import CreateView

def cadastroTurma(request):
    status = request.GET.get('status')
    form = turmaForm()
    return render(request, 'cadastro_turma.html', {'status':status, 'form':form})

def cadastroAnexo(request):
    status = request.GET.get('status')
    return render(request, 'anexo_material.html', {'status':status})

def cadastroChamada(request):
    status = request.GET.get('status')
    return render(request, 'chamada.html', {'status':status})

class turmaCreateView(CreateView):
    model = Turma
    form_class = turmaForm
    success_url = '/turma/cadastro/?status=0'
    template_name = "cadastro_turma.html"


'''def validaCadastroTurma(request):
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
        return redirect('/turma/cadastro/?status=10')'''