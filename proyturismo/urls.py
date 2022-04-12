from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from proyturismo.views import transportedeleteview, transportelistview, clientes, transportecreateview, transporteupdateview

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name='login'),


    path('destinoturistico',views.destinoturistico,name='destinoturistico'),
    path('destinoturistico/crear',views.creardestinoturistico,name='creardestinoturistico'),
    path('destinoturistico/editar',views.editardestinoturistico,name='editardestinoturistico'),
    

    path('boleto',views.boleto,name='boleto'),
    
    # Cliente
    path('cliente/', clientes.as_view(), name='cliente'),
    
    # Transporte
    path('transporte/', transportelistview.as_view(), name='transporte' ),
    path('transporte/crear/', transportecreateview.as_view(), name='creartransporte'),
    path('transporte/editar/<int:pk>', transporteupdateview.as_view(), name='editartransporte'),
    path('transporte/eliminar/<int:pk>', transportedeleteview.as_view(), name='eliminartransporte'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
