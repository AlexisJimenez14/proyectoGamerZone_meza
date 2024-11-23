from django.urls import path, include
from tienda_app import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path('productos/asus/', views.asus, name='asus'),
    path('productos/hp/', views.hp, name='hp'),
    path('productos/dell/', views.dell, name='dell'),
    path('productos/alienware/', views.alienware, name='alienware'),
    path('productos/productosGeneral/', views.productosGeneral, name='productosGeneral'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_carrito/<str:id_productos>/', views.agregar_carrito, name='agregar_carrito'),#nuevo carrito
    path('eliminar_carrito/<str:id_productos>/', views.eliminar_carrito, name='eliminar_carrito'),#nuevo carrito
    path('registro/', views.registro, name='registro'),
    path('login/', views.inicio_sesion, name='inicio_sesion'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)