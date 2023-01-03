from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Boletim1Bimestre, Boletim2Bimestre, Boletim3Bimestre, Boletim4Bimestre
from aluno.models import Aluno

def boletim(request):
    return render(request,'boletim.html')

def AdicionarNota1b(request):
    status = request.GET.get('status')
    alu = Aluno.objects.all()
    return render(request, 'boletim1b.html', {'status':status,'alu':alu})

def AdicionarNota2b(request):
    status = request.GET.get('status')
    alu = Aluno.objects.all()
    return render(request, 'boletim2b.html', {'status':status,'alu':alu})

def AdicionarNota3b(request):
    status = request.GET.get('status')
    alu = Aluno.objects.all()
    return render(request, 'boletim3b.html', {'status':status,'alu':alu})

def AdicionarNota4b(request):
    status = request.GET.get('status')
    alu = Aluno.objects.all()
    return render(request, 'boletim4b.html', {'status':status,'alu':alu})


def ValidaBoletim1(request):
    nome_aluno_boletim = request.POST.get('nome_aluno_boletim')
    nota1b1 = request.POST.get('1nota1')
    nota2b1 = request.POST.get('2nota1')
    nota3b1 = request.POST.get('3nota1')
    bimestral1 = request.POST.get('b1')
    media1 = request.POST.get('m1')

    try:
        boletim1 = Boletim1Bimestre(nome_aluno_boletim=nome_aluno_boletim,nota1b1=nota1b1,nota2b1=nota2b1,nota3b1=nota3b1,bimestral1=bimestral1, media1=media1)
        boletim1.save()
    except:
        return redirect('/boletim/1bimestre/?status=0')
    

def ValidaBoletim2(request):
    nome_aluno_boletim = request.POST.get('nome_aluno_boletim')
    nota1b2 = request.POST.get('1nota2')
    nota2b2 = request.POST.get('2nota2')
    nota3b2 = request.POST.get('3nota2')
    bimestral2 = request.POST.get('b2')
    media2 = request.POST.get('m2')

    try:
        boletim2 = Boletim2Bimestre(nome_aluno_boletim=nome_aluno_boletim,nota1b2=nota1b2,nota2b2=nota2b2,nota3b2=nota3b2,bimestral2=bimestral2, media2=media2)
        boletim2.save()
    except:
        return redirect('/boletim/2bimestre/?status=0')

def ValidaBoletim3(request):
    nome_aluno_boletim = request.POST.get('nome_aluno_boletim')
    nota1b3 = request.POST.get('1nota3')
    nota2b3 = request.POST.get('2nota3')
    nota3b3 = request.POST.get('3nota3')
    bimestral3 = request.POST.get('b3')
    media3 = request.POST.get('m3')

    try:
        boletim3 = Boletim3Bimestre(nome_aluno_boletim=nome_aluno_boletim,nota1b3=nota1b3,nota2b1=nota2b3,nota3b3=nota3b3,bimestral3=bimestral3, media3=media3)
        boletim3.save()
    except:
        return redirect('/boletim/3bimestre/?status=0')

def ValidaBoletim4(request):
    nome_aluno_boletim = request.POST.get('nome_aluno_boletim')
    nota1b4 = request.POST.get('1nota4')
    nota2b4 = request.POST.get('2nota4')
    nota3b4 = request.POST.get('3nota4')
    bimestral4 = request.POST.get('b4')
    media4 = request.POST.get('m4')

    mediafinal = request.POST.get('mediafinal')

    try:
        boletim4 = Boletim4Bimestre(nome_aluno_boletim=nome_aluno_boletim,nota1b4=nota1b4,nota2b4=nota2b4,nota3b4=nota3b4,bimestral4=bimestral4, media4=media4, mediafinal=mediafinal)
        boletim4.save()
    except:
        return redirect('/boletim/4bimestre/?status=0')