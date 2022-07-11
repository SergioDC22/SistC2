from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Felicidades, Se logueo correctamente {username}!.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

@login_required
def index(request):
    return render(request, 'index.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')
# APARTADO CLIENTES

@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index2.html', {'clientes': clientes})

@login_required
def inactivosC(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/inactivosC.html', {'clientes': clientes})

@login_required
def crearC(request):
    formulario = ClienteForm(request.POST or None,
                            request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,"Creado Correctamente")
        return redirect('clientes')
    return render(request, 'clientes/crearC.html', {'formulario': formulario})

@login_required
def editarC(request, id):
    cliente = Cliente.objects.get(idCli=id)
    formulario = ClienteForm(request.POST or None,
                             request.FILES or None, instance=cliente)

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/editarC.html', {'formulario': formulario})

@login_required
def eliminarC(request, idCli):
    cliente = Cliente.objects.get(idCli=idCli)
    cliente.isEstado = False
    cliente.save()
    messages.success(request,'Se cambio al estado INACTIVO Correctamente')
    return redirect('clientes')

@login_required
def activarC(request, idCli):
    cliente = Cliente.objects.get(idCli=idCli)
    cliente.isEstado = True
    cliente.save()
    messages.success(request,'Se cambio al estado ACTIVO Correctamente')
    return redirect('clientes')

