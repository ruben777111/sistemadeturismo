from django.views.generic import ListView
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
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

class transporte(ListView):
    model = Transporte
    template_name = 'transporte/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Transportes'
        context['pestaña'] = 'Listado de Transportes'
        return context
