from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno

def cadastroAluno(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_aluno.html', {'status':status})

def validaCadastroAluno(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    rg = request.POST.get('rg')
    email = request.POST.get('email')
    endereco = request.POST.get('endereco')
    contato = request.POST.get('telefone')
    turno = request.POST.get('turno')
    departamento = request.POST.get('departamento')
    senha = request.POST.get('senha')
    confirm_senha = request.POST.get('confirm-senha')

    aluno = Aluno.objects.filter(email=email).filter(cpf=cpf)

    if len(nome.strip())==0 or len(email.strip())==0:
        return redirect('/aluno/cadastro/?status=1')

    if len(aluno)>0:
        return redirect('/aluno/cadastro/?status=2')

    if len(nome)<3:
        return redirect('/aluno/cadastro/?status=3')

    if nome.isdigit()==True:
        return redirect('/aluno/cadastro/?status=4')

    if len(cpf)<11:
        return redirect('/aluno/cadastro/?status=5')
    
    if len(rg)<7:
        return redirect('/aluno/cadastro/?status=6')

    if len(endereco)<5:
        return redirect('/aluno/cadastro/?status=7')

    if '@' not in email:
        return redirect('/aluno/cadastro/?status=8')


    try:

        aluno = Aluno(nome=nome, cpf=cpf,rg=rg, email=email, endereco=endereco,contato=contato, turno=turno)
        aluno.save()
        return redirect('/aluno/cadastro/?status=0')
    except:
        return redirect('/aluno/cadastro/?status=10')

    return HttpResponse(f"{nome},{turno}")

def listagemAluno(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'listagem_aluno.html', {'alunos':alunos})

def verAluno(request,id):
    alunos = Aluno.objects.get(id=id)
    return render(request, 'visualizar_aluno.html',{'aluno': alunos})
