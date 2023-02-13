from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Aluno
from .forms import alunoForm
from django.views.generic import DeleteView, UpdateView, ListView, CreateView

def listagemAluno(request):
    alunos = Aluno.objects.all().order_by('nome_aluno')
    status = request.GET.get('status')
    return render(request, 'listagem_aluno.html', {'alunos':alunos,'status':status})

class AlunoCreateView(CreateView):
    model = Aluno
    template_name = "cadastro_aluno.html"
    form_class = alunoForm
    success_url = '/aluno/cadastro/?status=0'


class verAluno(ListView):
    model = Aluno
    template_name = "visualizar_aluno.html"

class deleteAluno(DeleteView):
    model = Aluno
    template_name = "delete_aluno.html"
    success_url = '/aluno/listagem/?status=0'

class editarAluno(UpdateView):
    model = Aluno
    form_class = alunoForm
    template_name = "editar_aluno.html"
    success_url = '/aluno/listagem/?status=1'

    

