from django.contrib import admin
from .models import Boleto, Destinoturistico, Cliente, Transporte
# Register your models here.
admin.site.register(Destinoturistico)
admin.site.register(Cliente)
admin.site.register(Boleto)
admin.site.register(Transporte)
