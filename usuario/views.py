from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Usuario, Users
from django.shortcuts import redirect
from hashlib import sha256
#from django.contrib.auth.models import User
from django.contrib import auth


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    rg = request.POST.get('rg')
    email = request.POST.get('email')
    endereco = request.POST.get('endereco')
    contato = request.POST.get('telefone')
    departamento = request.POST.get('departamento')
    senha = request.POST.get('senha')
    confirm_senha = request.POST.get('confirm-senha')

    '''
    usuario = Usuario.objects.filter(email=email).filter(cpf=cpf)
    user = Users.objects.filter(email=email)
    if user.exists():
        return redirect('/auth/cadastro/?status=1')

    if len(nome.strip())==0 or len(email.strip())==0:
        return redirect('/auth/cadastro/?status=1')

    if len(usuario)>0:
        return redirect('/auth/cadastro/?status=2')

    if len(nome)<3:
        return redirect('/auth/cadastro/?status=3')

    if nome.isdigit()==True:
        return redirect('/auth/cadastro/?status=4')

    if len(cpf)<11:
        return redirect('/auth/cadastro/?status=5')
    
    if len(rg)<7:
        return redirect('/auth/cadastro/?status=6')

    if len(endereco)<5:
        return redirect('/auth/cadastro/?status=7')

    if '@' not in email:
        return redirect('/auth/cadastro/?status=8')

    if len(senha)<8:
        return redirect('/auth/cadastro/?status=9')

    '''

    try:
        user = Users.objects.create_user(username=cpf,email=email,password=senha,first_name=nome, departamento_user=departamento, contato_user=contato, rg_user=rg, cpf_user=cpf)
        usuario = Usuario(nome=nome, cpf=cpf,rg=rg, email=email, endereco=endereco,contato=contato, departamento=departamento, senha=senha, confirm_senha=confirm_senha)
        usuario.save()
        user.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=10')

def login(request):
    status = request.GET.get('status')
    return render(request,'login.html', {'status':status})

def valida_login(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return render(request,'login.html')
    elif request.method=="POST":
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        user = auth.authenticate(username=cpf,password=senha)
        if not user:
            return redirect('/auth/login/?status=1')
        auth.login(request,user)
        return redirect('home')
    '''cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()  

    usuario = Usuario.objects.filter(cpf=cpf).filter(senha=senha)

    if len(usuario)==0:
        return redirect('/auth/login/?status=1')
    elif len(usuario)>0:
        request.session['usuario'] = usuario[0].id
        return redirect('/home/')

    return HttpResponse(f'{cpf},{senha}')'''

def listagem(request):
    usuarios = Usuario.objects.all().order_by('nome')
    return render(request, 'listagem.html', {'usuarios':usuarios})

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')