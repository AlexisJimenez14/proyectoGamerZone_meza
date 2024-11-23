from django.shortcuts import render, redirect
from .models import Producto
from django.http import JsonResponse
#login
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#login


# Create your views here.
def inicio_vista(request):
    losproductos=Producto.objects.all()
    return render(request,"index.html",{"misproductos":losproductos})

def productosGeneral(request):
    losproductos=Producto.objects.all()
    return render(request, 'productos/productosGeneral.html',{"misproductos":losproductos})

def asus(request):
    losproductos=Producto.objects.all()
    return render(request, 'productos/asus.html',{"misproductos":losproductos})

def hp(request):
    losproductos=Producto.objects.all()
    return render(request, 'productos/hp.html',{"misproductos":losproductos})

def dell(request):
    losproductos=Producto.objects.all()
    return render(request, 'productos/dell.html',{"misproductos":losproductos})

def alienware(request):
    losproductos=Producto.objects.all()
    return render(request, 'productos/alienware.html',{"misproductos":losproductos})


# Almacena los productos del carrito temporalmente en la sesión
def carrito(request):
    carrito = request.session.get('carrito', {})
    productos_carrito = []
    total = 0

    for id_producto, cantidad in carrito.items():
        producto = Producto.objects.get(id_productos=id_producto)
        subtotal = producto.precio * cantidad
        productos_carrito.append({'producto': producto, 'cantidad': cantidad, 'subtotal': subtotal})
        total += subtotal

    return render(request, 'productos/carrito.html', {'productos_carrito': productos_carrito, 'total': total})

# Agregar productos al carrito, con javascript
@login_required
def agregar_carrito(request, id_productos):
    carrito = request.session.get('carrito', {})
    carrito[id_productos] = carrito.get(id_productos, 0) + 1
    request.session['carrito'] = carrito

    total_items = sum(carrito.values())  # Contar la cantidad total de productos en el carrito
    return JsonResponse({'status': 'success', 'total_items': total_items})

# Eliminar productos del carrito
def eliminar_carrito(request, id_productos):
    carrito = request.session.get('carrito', {})
    if id_productos in carrito:
        del carrito[id_productos]
    request.session['carrito'] = carrito
    return redirect('carrito')



#login

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente tras el registro
            return redirect('inicio_vista')  # Cambia por la página a la que quieres redirigir después
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


def inicio_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio_vista')  # Cambia por la página que prefieras
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_vista')  # Redirige al inicio o donde prefieras

#login