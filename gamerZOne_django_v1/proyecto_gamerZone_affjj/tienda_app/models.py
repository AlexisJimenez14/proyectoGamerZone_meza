from django.db import models

# Create your models here.
class Producto(models.Model):
    id_productos=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, default="Descripción predeterminada")
    stock= models.IntegerField()
    precio= models.IntegerField()
    lote=models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    ASUS = 'Asus'
    HP = 'HP'
    DELL = 'Dell'
    ALIENWARE = 'Alienware'

    MARCAS_CHOICES = [
        (ASUS, 'Asus'),
        (HP, 'HP'),
        (DELL, 'Dell'),
        (ALIENWARE, 'Alienware'),
    ]

    # Campo para la marca
    marca = models.CharField(
        max_length=20,
        choices=MARCAS_CHOICES,
        default=ASUS,  # Marca predeterminada si no se selecciona ninguna
    )
    

    def __str__(self):
        return self.nombre


#nuevo carrito
class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.cantidad * self.producto.precio