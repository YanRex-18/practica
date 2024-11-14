from django.db import models

# Create your models here.

class Producto(models.Model):
    Nombre=models.CharField(max_length=50, blank=True,null=False,verbose_name='Nombre del producto')
    description=models.TextField(verbose_name='Descripción del producto')
    precio=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Precio del producto')
    fecha_creacion=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    def __str__(self):
        return self.Nombre 
