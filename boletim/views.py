from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Boletim

def AdicionarNota(request):
    status = request.GET.get('status')
    return render(request, 'boletim.html', {'status':status})

def ValidaBoletim(request):
    nota1b1 = request.POST.get('1nota1')
    nota2b1 = request.POST.get('2nota1')
    nota3b1 = request.POST.get('3nota1')
    bimestral1 = request.POST.get('b1')
    media1 = request.POST.get('m1')

    nota1b2 = request.POST.get('1nota2')
    nota2b2 = request.POST.get('2nota2')
    nota3b2 = request.POST.get('3nota2')
    bimestral2 = request.POST.get('b2')
    media2 = request.POST.get('m2')

    nota1b3 = int(request.POST.get('1nota3'))
    nota2b3 = int(request.POST.get('2nota3'))
    nota3b3 = int(request.POST.get('3nota3'))
    bimestral3 = int(request.POST.get('b3'))
    media3 = int(request.POST.get('m3'))

    nota1b4 = int(request.POST.get('1nota4'))
    nota2b4 = int(request.POST.get('2nota4'))
    nota3b4 = int(request.POST.get('3nota4'))
    bimestral4 = int(request.POST.get('b4'))
    media4 = int(request.POST.get('m4'))

    mediafinal = int(request.POST.get('mediafinal'))

    boletim = Boletim(
        nota1b1=nota1b1, nota2b1=nota2b1, nota3b1=nota1b1, bimestral1=bimestral1, media1=media1,
        nota1b2=nota1b2, nota2b2=nota2b2, nota3b2=nota3b2, bimestral2=bimestral2, media2=media2,
        nota1b3=nota1b3, nota2b3=nota2b3, nota3b3=nota3b3, bimestral3=bimestral3, media3=media3,
        nota1b4=nota1b4, nota2b4=nota2b4, nota3b4=nota3b4, bimestral4=bimestral4, media4=media4,
        mediafinal=mediafinal
    )
    boletim.save()
    

    if 0<nota1b1>100 or 0<nota2b1>100 or 0<nota3b1>100:
        return redirect('/boletim/novo/?status=1')
    if 0<nota1b2>100 or 0<nota2b2>100 or 0<nota3b2>100:
        return redirect('/boletim/novo/?status=1')
    if 0<nota1b3>100 or 0<nota2b3>100 or 0<nota3b3>100:
        return redirect('/boletim/novo/?status=1')
    if 0<nota1b4>100 or 0<nota2b4>100 or 0<nota3b4>100:
        return redirect('/boletim/novo/?status=1')
    if 0<media1>100 or 0<media2>100 or 0<media3 or 0<media4>100:
        return redirect('/boletim/novo/?status=1')
    if 0<bimestral1>100 or 0<bimestral2>100 or 0<bimestral3 or 0<bimestral4>100:
        return redirect('/boletim/novo/?status=1')
    else:
        return redirect('/boletim/novo/?status=0')