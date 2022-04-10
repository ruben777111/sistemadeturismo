from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name='login'),


    path('destinoturistico',views.destinoturistico,name='destinoturistico'),
    path('destinoturistico/crear',views.creardestinoturistico,name='creardestinoturistico'),
    path('destinoturistico/editar',views.editardestinoturistico,name='editardestinoturistico'),
    
  
    path('boleto',views.boleto,name='boleto'),

 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
