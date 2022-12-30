from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuario.models import Usuario

def home(request):
    return render(request,'index.html')
    '''if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        #return HttpResponse(f"olá, {usuario}")
    else:
        return redirect('/auth/login/?status=2')'''