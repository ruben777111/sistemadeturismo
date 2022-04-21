from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from proyturismo.views import *

urlpatterns=[
    path('',LoginViewUser.as_view(), name='login'),
    # path('', LoginViewUser2.as_view()),
    # path('login', LoginViewUser2.as_view(), name='login'),
    # path('',loginUser),  # Momentáneo
    # path('login',loginUser, name='login'),
    path('logout/', logoutuser, name='logout' ),

    # Destinoturistico
    path('destinoturistico',views.destinoturistico,name='destinoturistico'),
    path('destinoturistico/crear',views.creardestinoturistico,name='creardestinoturistico'),
    path('destinoturistico/editar',views.editardestinoturistico,name='editardestinoturistico'),
    path('eliminardestino/<int:id>',views.eliminardestino,name='eliminardestino'),
    path('destinoturistico/editar/<int:id>',views.editardestinoturistico,name='editardestinoturistico'),
    
    #Boleto
    path('boleto',views.boleto,name='boleto'),
    path('boleto/crearboletocliente',views.crearboletocliente,name='crearboletocliente'),
    
    # Cliente
    path('cliente/', clienteslistView.as_view(), name='cliente'),
    path('cliente/crear/', clientescreateview.as_view(), name='crearcliente'),
    path('cliente/editar/<int:pk>', clienteupdateview.as_view(), name='editarcliente'),
    path('cliente/eliminar/<int:pk>', clientedeleteview.as_view(), name='eliminarcliente'),
    
    
    # Transporte
    path('transporte/', transportelistview.as_view(), name='transporte' ),
    path('transporte/crear/', transportecreateview.as_view(), name='creartransporte'),
    path('transporte/editar/<int:pk>', transporteupdateview.as_view(), name='editartransporte'),
    path('transporte/eliminar/<int:pk>', transportedeleteview.as_view(), name='eliminartransporte'),

    #Pruebas
    path('test/', pruebas, name='prueba')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
