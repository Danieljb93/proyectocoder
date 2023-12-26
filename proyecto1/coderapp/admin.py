from django.contrib import admin

from coderapp.models import Vendedor, Cliente, Producto, Venta

admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Venta)

