from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinoturistico

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



"""vista para transporte"""
