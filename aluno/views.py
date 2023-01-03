from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Aluno
from .forms import alunoForm
from django.views.generic import DeleteView, UpdateView

#Aluno
def cadastroAluno(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_aluno.html', {'status':status})

def validaCadastroAluno(request):
    nome_aluno = request.POST.get('nome_aluno')
    cpf_aluno = request.POST.get('cpf_aluno')
    rg_aluno = request.POST.get('rg_aluno')
    email_aluno = request.POST.get('email_aluno')
    endereco_aluno = request.POST.get('endereco_aluno')
    contato_aluno = request.POST.get('contato_aluno')
    turno_aluno = request.POST.get('turno_aluno')
    data_nascimento_aluno = request.POST.get('data_nascimento_aluno')
    data_entrada_aluno = request.POST.get('data_entrada_aluno')
    raca_aluno = request.POST.get('raca_aluno')
    sexo_aluno = request.POST.get('sexo_aluno')

    '''
    aluno = Aluno.objects.filter(email_aluno=email_aluno).filter(cpf_aluno=cpf_aluno)

    if len(nome_aluno.strip())==0 or len(email_aluno.strip())==0:
        return redirect('aluno/cadastro/?status=1')

    if len(aluno)>0:
        return redirect('/aluno/cadastro/?status=2')

    if len(nome_aluno)<3:
        return redirect('/aluno/cadastro/?status=3')

    if nome_aluno.isdigit()==True:
        return redirect('/aluno/cadastro/?status=4')

    if len(cpf_aluno)<11:
        return redirect('/aluno/cadastro/?status=5')
    
    if len(rg_aluno)<7:
        return redirect('/aluno/cadastro/?status=6')

    if len(endereco_aluno)<5:
        return redirect('/aluno/cadastro/?status=7')

    if '@' not in email_aluno:
        return redirect('/aluno/cadastro/?status=8')
    '''

    try:
        alunos = Aluno(nome_aluno=nome_aluno, cpf_aluno=cpf_aluno,rg_aluno=rg_aluno, email_aluno=email_aluno, 
        endereco_aluno=endereco_aluno,contato_aluno=contato_aluno, turno_aluno=turno_aluno,data_nascimento_aluno=data_nascimento_aluno,
        data_entrada_aluno=data_entrada_aluno,raca_aluno=raca_aluno,sexo_aluno=sexo_aluno)

        alunos.save()
        return redirect('/aluno/cadastro/?status=0')
    except:
        return redirect('/aluno/cadastro/?status=10')

    #return HttpResponse(f"{nome},{turno}")

def listagemAluno(request):
    alunos = Aluno.objects.all().order_by('nome_aluno')
    status = request.GET.get('status')
    return render(request, 'listagem_aluno.html', {'alunos':alunos,'status':status})

def verAluno(request,id):
    alunos = Aluno.objects.get(id=id)
    return render(request, 'visualizar_aluno.html',{'aluno': alunos})

class deleteAluno(DeleteView):
    model = Aluno
    template_name = "delete_aluno.html"
    success_url = '/aluno/listagem/?status=0'

class editarAluno(UpdateView):
    model = Aluno
    form_class = alunoForm
    template_name = "editar_aluno.html"
    success_url = '/aluno/listagem/?status=1'

    

