from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import ProductoMedico
from .forms import *
from .controller import Controller
from .producto import Producto
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate,login,logout
from django.contrib.auth.decorators import login_required


def Index(request):
    return render(request, 'index.html')

def Nosotros(request):
    return render(request, 'nosotros.html')

def Contacto(request):
    data={
        'form':ContactForm()
    }
    
    if request.method == 'POST': 
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
    return render(request, 'contacto.html',data)

def Asesoria(request):
    return render(request, 'asesoria.html')

def Servicio(request):
    return render(request, 'servicio.html')

def Equipos(request):
    variable =  {
        'mensaje': '',
        'lista': '',
    }
    controller = Controller()
    print("hola")
    try:
        lista = controller.buscarTodo
        print(lista)
        variable['lista'] = lista
        variable['mensaje'] = 'con datos'
    except:
        variable['mensaje'] = 'sin datos'
    return render(request, 'equipos.html',variable)

def Perfil(request):
    return render(request, 'perfil.html')

def Inventario(request):
    return render(request, 'inventario.html')

def subir_imagen(request, p_numb):
    producto = get_object_or_404(ProductoMedico, p_numb=p_numb)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('subir-imagen.html', p_numb=p_numb)
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'subir_imagen.html', {'form': form, 'producto': producto})
@login_required
def Bodega(request):
    variable = {
        'mensaje': '',
        'lista': '',
    }
    controller = Controller()
    try:
        lista = controller.buscarTodo()  # Llamada a la función buscarTodo()
        variable['lista'] = lista
        variable['mensaje'] = 'con datos'
    except:
        variable['mensaje'] = 'sin datos'

    if request.method == 'POST':
        codigo = request.POST.get('codigo_producto')
        resultado = controller.eliminarProducto(codigo)
        if resultado:
            messages.success(request, 'Producto eliminado correctamente')
        else:
            messages.error(request, 'Error al eliminar el producto')
    return render(request, 'bodega.html', variable)
@login_required
def agregar_producto(request):
    return render(request, 'agregar.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvenido')
            return redirect('/')
        else:
            messages.error(request, 'Credenciales inválidas')
            
    return render(request, 'registro/login.html')
def Cerrar_sesion(request):
    logout(request)
    return redirect('/')

def registro(request):
    data ={
        'form':CustomUserCreationForm()
    }  
    if request.method == 'POST': 
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
        data["form"] = formulario
    return render(request, 'registro/registro.html',data)



def mercadopago(request):
    controller = Controller()
    data = {
        'mensaje': '',
        'lista': [],
        'preference_id': '',
    }
    try:
        preference = controller.pagar()
        data['preference_id'] = preference['response']['id']
        data['lista'] = controller.buscarTodo()
        data['mensaje'] = 'OK'
    except Exception as e:
        data['mensaje'] = f'Error: {e}'
        data['lista'] = controller.buscarTodo()  # aún muestra productos si falla pago
    return render(request, 'equipos.html', data)
def buscarProducto(request):
    controller = Controller()
    codigo = request.POST.get('codigo')
    producto = controller.buscarUnaBodega(codigo)
    return JsonResponse({
        'codigo': producto.id_producto,
        'nombre': producto.nombre,
        'stock': producto.stock,
        'precio': producto.precio,
        'btu': producto.btu,
        'marca': producto.marca
    })
@login_required
def actualizarProducto(request):
    controller = Controller()
    codigo = request.POST.get('codigo_oculto')
    stock = request.POST.get('stock_disponible')
    precio = request.POST.get('precio')
    resultado = controller.actualizarStock(codigo, stock,precio)
    return JsonResponse({
        'mensaje': resultado
    })
@login_required
def actualizar (request):
    variable =  {
        'mensaje': '',
        'lista': '',
    }
    controller = Controller()
    try:
        lista = controller.buscarTodo
        variable['lista'] = lista
        variable['mensaje'] = 'con datos'
    except:
        variable['mensaje'] = 'sin datos'
    return render(request, 'actualizar.html')
@login_required
def eliminarProducto(request, id_producto):
    if request.method == 'POST':
        controller = Controller()
        resultado = controller.eliminarProducto(id_producto)
        
        if resultado:
            return JsonResponse({'mensaje': 'Producto eliminado correctamente'})
        else:
            return JsonResponse({'mensaje': 'Error al eliminar el producto'})

    return JsonResponse({'mensaje': 'Error: solicitud no válida'})
@login_required
def ingresarProducto(request):
    if request.method == 'POST':
        controller = Controller()
        precio = request.POST.get('precio')
        btu = request.POST.get('btu')
        marca = request.POST.get('marca')
        nombre = request.POST.get('nombre')
        stock = request.POST.get('stock')
        resultado = controller.IngresarProducto(precio, btu, marca, nombre, stock)
        if resultado:
            return JsonResponse({'mensaje': 'Producto agregado correctamente'})
        else:
            return JsonResponse({'mensaje': 'Error al agregar el producto'})
    return JsonResponse({'mensaje': 'Error: solicitud no válida'})