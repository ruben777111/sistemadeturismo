from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse

from proyturismo.forms import TransporteForm
from .models import Cliente, Destinoturistico, Transporte

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>bienveenido</h1>")
def login(request):
    return render(request,'ingresar/login.html')

"""vista para destinoturistico"""
def destinoturistico(request):
    destino=Destinoturistico.objects.all()

    return render(request,'destinoturistico/index.html',{'destino':destino})
    
def creardestinoturistico(request):
    return render(request,'destinoturistico/crear.html')

def editardestinoturistico(request):
    return render(request,'destinoturistico/editar.html')




"""vista para boleto"""
def boleto(request):
    return render(request,'boleto/index.html')




"""vista para cliente"""
class clientes(ListView):
    model = Cliente
    template_name = 'cliente/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['pestaña'] = 'Listado de Clientes'
        return context



"""vista para transporte"""

class transportelistview(ListView):  # ListView
    model = Transporte
    template_name = 'transporte/index.html'
    
    # def dispatch(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         return redirect('')
    
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
    
    def get_context_data(self, **kwargs):  # Context Parameters
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Transporte'
        context['pestaña'] = 'Editar Tranporte'
        context['boton'] = 'Actualizar Datos'
        return context


class transportedeleteview(DeleteView):
    model = Transporte
    template_name = 'transporte/eliminar.html'
    success_url = reverse_lazy('transporte')
    
    def get_context_data(self, **kwargs):  # Context Parameters
        context = super().get_context_data(**kwargs)
        context['titulo'] = '¿Eliminar Transporte?'
        context['pestaña'] = 'Eliminar Tranporte'
        context['list_url'] = reverse_lazy('transporte')
        context['btnsi'] = 'Si, aceptar'
        context['btnno'] = 'Cancelar'
        
        
        return context
    