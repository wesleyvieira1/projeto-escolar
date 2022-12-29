from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno

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
        return redirect('aluno/cadastro/?status=1')

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

        aluno = Aluno(nome_aluno=nome, cpf_aluno=cpf,rg_aluno=rg, email_aluno=email, endereco_aluno=endereco,contato_aluno=contato, turno_aluno=turno)
        aluno.save()
        return redirect('/aluno/cadastro/?status=0')
    except:
        return redirect('/aluno/cadastro/?status=10')

    return HttpResponse(f"{nome},{turno}")

def listagemAluno(request):
    alunos = Aluno.objects.all().order_by('nome_aluno')
    return render(request, 'listagem_aluno.html', {'alunos':alunos})

def verAluno(request,id):
    alunos = Aluno.objects.get(id=id)
    return render(request, 'visualizar_aluno.html',{'aluno': alunos})
