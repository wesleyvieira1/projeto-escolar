from django.shortcuts import render

def cadastroMensalidade(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_mensalidade.html', {'status':status})

def listagemMensaliudade(request):
    status = request.GET.get('status')
    return render(request, 'listagem_mensalidade.html', {'status':status})