from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno, Disciplina, Professor

#Aluno
def cadastroAluno(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_aluno.html', {'status':status})

def validaCadastroAluno(request):
    nome = request.POST.get('nome_aluno')
    cpf = request.POST.get('cpf_aluno')
    rg = request.POST.get('rg_aluno')
    email = request.POST.get('email_aluno')
    endereco = request.POST.get('endereco_aluno')
    contato = request.POST.get('telefone_aluno')
    turno = request.POST.get('turno_aluno')


    aluno = Aluno.objects.filter(email_aluno=email).filter(cpf_aluno=cpf)

    if len(nome.strip())==0 or len(email.strip())==0:
        return redirect('academico/aluno/cadastro/?status=1')

    if len(aluno)>0:
        return redirect('academico/aluno/cadastro/?status=2')

    if len(nome)<3:
        return redirect('academico/aluno/cadastro/?status=3')

    if nome.isdigit()==True:
        return redirect('academico/aluno/cadastro/?status=4')

    if len(cpf)<11:
        return redirect('academico/aluno/cadastro/?status=5')
    
    if len(rg)<7:
        return redirect('academico/cadastro/?status=6')

    if len(endereco)<5:
        return redirect('academico/aluno/cadastro/?status=7')

    if '@' not in email:
        return redirect('academico/aluno/cadastro/?status=8')


    try:

        aluno = Aluno(nome_aluno=nome, cpf_aluno=cpf,rg_aluno=rg, email_aluno=email, endereco_aluno=endereco,contato_aluno=contato, turno_aluno=turno)
        aluno.save()
        return redirect('academico/aluno/cadastro/?status=0')
    except:
        return redirect('academico/aluno/cadastro/?status=10')

    return HttpResponse(f"{nome},{turno}")

def listagemAluno(request):
    alunos = Aluno.objects.all().order_by('nome_aluno')
    return render(request, 'listagem_aluno.html', {'alunos':alunos})

def verAluno(request,id):
    alunos = Aluno.objects.get(id=id)
    return render(request, 'visualizar_aluno.html',{'aluno': alunos})

#Professor

def cadastroProfessor(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_professor.html', {'status':status})

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
        return redirect('academico/professor/cadastro/?status=0')
    except:
        return redirect('academico/professor/cadastro/?status=10')

def listagemProfessor(request):
    professores = Professor.objects.all().order_by('nome_prof')
    return render(request, 'listagem_professor.html', {'professores':professores},)

#Disciplina

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
        return redirect('/academico/disciplina/cadastro/?status=0')
    except:
        return redirect('/academico/disciplina/cadastro/?status=10')


#Turma
def cadastroTurma(request):
    status = request.GET.get('status')
    dicipls = Disciplina.objects.all()
    return render(request, 'cadastro_turma.html', {'status':status, 'dicipls':dicipls})

def validaCadastroTurma(request):
    ano_turma = request.POST.get('ano_turma')
    horario_inicio_turma = request.POST.get('hrI')
    horario_fim_turma = request.POST.get('hrF')
    etapa_turma = request.POST.get('etapa_turma')
    disciplina_turma = request.POST.get('disciplina_turma')
    dia_turma = request.POST.get('dia_turma')
