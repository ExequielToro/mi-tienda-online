"""
URL configuration for MedServ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from MedServ_app.views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='Index'),
    path('Nosotros', Nosotros, name='Nosotros'),
    path('Contacto', Contacto, name='Contacto'),
    path('Asesoria', Asesoria, name='Asesoria'),
    path('Servicio', Servicio, name='Servicio'),
    path('Equipos', mercadopago, name='Equipos'),
    path('Perfil', Perfil, name='Perfil'),
    path('Inventario', Inventario, name='Inventario'),
    path('producto/<int:p_numb>/subir-imagen/', subir_imagen, name='subir_imagen'),
    path('Bodega',Bodega,name='bodega'),
    path('accounts/login/', LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('logout', Cerrar_sesion, name='logout'),
    path('Pago',Equipos,name='Pago'),
    path('post/ajax/buscar',buscarProducto,name="post_buscar"),
    path('post/ajax/actualizar',actualizarProducto,name="post_actualizar"),
    path('actualizar/', actualizar, name="actualizar"),
    path('eliminar/<id_producto>', eliminarProducto, name="eliminar_producto"),
    path('ingresar-producto/',ingresarProducto, name='ingresar-producto'),
    path('agregar_producto/',agregar_producto, name='agregar_producto'),
    path('registro_usuario/',registro,name="registro_usuario"),
    
]

