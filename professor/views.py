from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Professor

def cadastroProfessor(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_professor.html', {'status':status})

def validaCadastroProfessor(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    rg = request.POST.get('rg')
    email = request.POST.get('email')
    endereco = request.POST.get('endereco')
    formacao = request.POST.get('formacao')
    contato = request.POST.get('telefone')
    turno = request.POST.get('turno')
    data_nascimento = request.POST.get('data_nascimento')
    data_entrada = request.POST.get('data_entrada')
    raca = request.POST.get('raca')
    sexo = request.POST.get('sexo')

    try:
        professor = Professor(nome=nome, cpf=cpf,rg=rg, email=email, endereco=endereco,
        contato=contato, turno=turno, data_nascimento=data_nascimento, data_entrada=data_entrada, 
        raca=raca, sexo=sexo, formacao=formacao)
        professor.save()
        return redirect('/professor/cadastro/?status=0')
    except:
        return redirect('/professor/cadastro/?status=10')

def listagemProfessor(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, 'listagem_professor.html', {'professores':professores})