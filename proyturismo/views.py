# Shortcuts
from django.shortcuts import render, redirect
# Html
from django.http import HttpResponse, HttpResponseRedirect
# Urls
from django.urls import reverse_lazy
# Decoradores
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.forms import ValidationError
# Vistas para CRUD
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Esto no sé
from proyturismo.forms import *
from .models import Cliente, Destinoturistico, Transporte, Boleto

# Create your views here.

def pruebas(request):
    return render(request, 'pruebas.html')


def inicio(request):
    return HttpResponse("<h1>bienveenido</h1>")

# ========================= LOGIN ======================================
class LoginViewUser(LoginView):
    template_name = 'ingresar/loginU.html'
    
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('boleto')
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Iniciar Sesión'
        return context


def logoutuser(request):
    logout(request)
    return redirect('login')


"""vista para destinoturistico"""


@login_required
def destinoturistico(request):
    destino = Destinoturistico.objects.all()

    return render(request, 'destinoturistico/index.html', {'destino': destino})

@csrf_exempt  # csrf token para enviar archivos
@login_required  # login requerido para entrar a esta vista
def creardestinoturistico(request):
    """request.FILES or None para recepcionar archivos"""
    formulario = destinoform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('destinoturistico')
    return render(request, 'destinoturistico/crear.html', {'formulario': formulario})


@login_required
def eliminardestino(request, id):
    destino = Destinoturistico.objects.get(iddestino=id)
    destino.delete()
    return redirect('destinoturistico')


@login_required
def editardestinoturistico(request, id):
    destino = Destinoturistico.objects.get(iddestino=id)
    formulario = destinoform(request.POST or None,
                            request.FILES or None, instance=destino)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('destinoturistico')
    return render(request, 'destinoturistico/editar.html', {'formulario': formulario})


"""vista para boleto"""


@login_required
def boleto(request):
    ventaboleto= Boleto.objects.all();
    return render(request, 'boleto/index.html', {'ventaboleto': ventaboleto})



@login_required
def crearboletocliente(request):

    formulario = boletoclienteform(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('destinoturistico')
    return render(request, 'boleto/formcliente.html', {'formulario': formulario})


"""vista para cliente"""


class clienteslistView(ListView):
    model = Cliente
    template_name = 'cliente/index.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Clientes'
        context['pestaña'] = 'Listado de Clientes'
        return context


class clientescreateview(CreateView):
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('cliente')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Cliente'
        context['pestaña'] = 'Nuevo Cliente'
        context['boton'] = 'Agregar Cliente'
        return context


class clienteupdateview(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('cliente')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['titulo'] = 'Editar Cliente'
        context['pestaña'] = 'Editar Cliente'
        context['boton'] = 'Actualizar Datos'
        return context


class clientedeleteview(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('cliente')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['titulo'] = '¿Eliminar Cliente?'
        context['pestaña'] = 'Eliminar Cliente'
        context['list_url'] = reverse_lazy('cliente')
        context['btnsi'] = 'Si, aceptar'
        context['btnno'] = 'Cancelar'
        return context


"""vista para transporte"""


class transportelistview(ListView):  # ListView
    model = Transporte
    template_name = 'transporte/index.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):  # Context Parameters
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Transportes'
        context['pestaña'] = 'Listado de Transportes'
        return context


class transportecreateview(CreateView):
    # model = Transporte  # Parece que esto no influye
    form_class = TransporteForm
    template_name = 'transporte/crear.html'
    success_url = reverse_lazy('transporte')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):  # Context Parameters
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nuevo Transporte'
        context['pestaña'] = 'Nuevo Tranporte'
        context['boton'] = 'Agregar Transporte'
        return context


class transporteupdateview(UpdateView):
    model = Transporte
    form_class = TransporteForm
    template_name = 'transporte/crear.html'
    success_url = reverse_lazy('transporte')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Transporte'
        context['pestaña'] = 'Editar Tranporte'
        context['boton'] = 'Actualizar Datos'
        return context


class transportedeleteview(DeleteView):
    model = Transporte
    template_name = 'transporte/eliminar.html'
    success_url = reverse_lazy('transporte')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):  # Context Parameters
        context = super().get_context_data(**kwargs)
        context['titulo'] = '¿Eliminar Transporte?'
        context['pestaña'] = 'Eliminar Tranporte'
        context['list_url'] = reverse_lazy('transporte')
        context['btnsi'] = 'Si, aceptar'
        context['btnno'] = 'Cancelar'

        return context
