from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Disciplina, Professor
from .forms import disciplinaForm
from django.views.generic import CreateView

#Professor

def cadastroProfessor(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_professor.html', {'status':status})

def cadastroBoletim(request):
    status = request.GET.get('status')
    return render(request, 'Boletim.html', {'status':status})

def validaCadastroProfessor(request):
    nome = request.POST.get('nome_prof')
    cpf = request.POST.get('cpf_prof')
    rg = request.POST.get('rg_prof')
    email = request.POST.get('email_prof')
    endereco = request.POST.get('endereco_prof')
    formacao = request.POST.get('formacao_prof')
    contato = request.POST.get('telefone_prof')
    turno = request.POST.get('turno_prof')
    data_nascimento = request.POST.get('data_nascimento_prof')
    data_entrada = request.POST.get('data_entrada_prof')
    raca = request.POST.get('raca_prof')
    sexo = request.POST.get('sexo_prof')

    try:
        professor = Professor(nome_prof=nome, cpf_prof=cpf,rg_prof=rg, email_prof=email, endereco_prof=endereco,
        contato_prof=contato, turno_prof=turno, data_nascimento_prof=data_nascimento, data_entrada_prof=data_entrada, 
        raca_prof=raca, sexo_prof=sexo, formacao_prof=formacao)
        professor.save()
        return redirect('acad/cadastro/?status=0')
    except:
        return redirect('acad/cadastro/?status=10')

def listagemProfessor(request):
    professores = Professor.objects.all().order_by('nome_prof')
    return render(request, 'listagem_professor.html', {'professores':professores},)

#Disciplina
def cadastroDisciplina(request):
    status = request.GET.get('status')
    form = disciplinaForm()
    return render(request, 'cadastro_disciplina.html', {'form':form, 'status':status})

class DisciplinaCreateView(CreateView):
    model = Disciplina
    form_class = disciplinaForm
    template_name = "cadastro_disciplina.html"
    success_url = '/acad/disciplina_cadastro/?status=0'



'''def validaCadastroDisciplina(request):
    nome_disciplina = request.POST.get('nome_disciplina')
    professor_disciplina = request.POST.get('professor_disciplina')
    
    disciplina = Disciplina(nome_disciplina=nome_disciplina, professor_disciplina=professor_disciplina)
    disciplina.save()
    try:
        disciplina = Disciplina(nome_disciplina=nome_disciplina, professor_disciplina=professor_disciplina)
        disciplina.save()
        return redirect('/disciplina/cadastro/?status=0')
    except:
        return redirect('/disciplina/cadastro/?status=10')'''

