from django.db import models

# Create your models here.
class Carrito(models.Model):
	total = models.DecimalField(max_digits=20, decimal_places=2)
	comprador = models.ForeignKey('User', related_name='carrito')
	checkedOut = models.BooleanField(default=False)
	timestamp = models.DateField(auto_now_add=True)

class CarritoItem(models.Model):
	carrito = models.ForeignKey('Carrito')
	item = models.ForeignKey('Item')
	cantidad = models.IntegerField(default=1)
	
class Item(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=255)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	categoria = models.ForeignKey('Categoria')
	existencia = models.IntegerField()
	tienda = models.ForeignKey('Tienda')

class Tienda(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=255)
	dueno = models.ForeignKey('User', 'tienda')

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)


