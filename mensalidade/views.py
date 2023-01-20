from django.shortcuts import render

def cadastroMensalidade(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_mensalidade.html', {'status':status})

