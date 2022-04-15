from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse

from proyturismo.forms import ClienteForm, TransporteForm, destinoform
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
    """request.FILES or None para recepcionar archivos"""
    formulario=destinoform(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('destinoturistico')
    return render(request,'destinoturistico/crear.html',{'formulario':formulario})



def eliminardestino(request,id):
    destino=Destinoturistico.objects.get(iddestino=id)
    destino.delete()
    return redirect('destinoturistico')

def editardestinoturistico(request,id):
    destino=Destinoturistico.objects.get(iddestino=id)
    formulario=destinoform(request.POST or None, request.FILES or None, instance=destino)
    if formulario.is_valid() and request.method =='POST':
        formulario.save()
        return redirect('destinoturistico')
    return render(request,'destinoturistico/editar.html',{'formulario':formulario})


"""vista para boleto"""
def boleto(request):
    return render(request,'boleto/index.html')




"""vista para cliente"""
class clienteslistView(ListView):
    model = Cliente
    template_name = 'cliente/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Clientes'
        context['pestaña'] = 'Listado de Clientes'
        return context

class clientescreateview(CreateView):
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('cliente')
    
    
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cliente'
        context['pestaña'] = 'Editar Cliente'
        context['boton'] = 'Actualizar Datos'
        return context
    
class clientedeleteview(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('cliente')
    
    
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
    