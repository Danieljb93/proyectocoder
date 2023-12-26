from django.db import models

class Vendedor(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Vendedores"
        ordering=["nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} -- {self.cantidad}"


class Venta(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeVenta = models.DateField()

    def __str__(self):
        return f"{self.nombre} -- {self.fechaDeVenta}"
    

