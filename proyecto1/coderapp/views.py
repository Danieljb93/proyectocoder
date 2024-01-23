from django.http import HttpResponse
from django.shortcuts import render

from coderapp.models import Vendedor, Producto, Cliente, Avatar
from coderapp.forms import VentaFormulario, NuevoVendedor, NuevoCliente, VendedorFormulario, AvatarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "index.html")

@login_required
def vendedores(request):
    if request.method == "POST":

        #leer los datos que vienen en el post

        datos_vendedor = VendedorFormulario(request.POST)

        print(datos_vendedor)

        if datos_vendedor.is_valid():
            
            datos = datos_vendedor.cleaned_data

            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            email = datos.get("email")

            vendedor = Vendedor(nombre=nombre, apellido=apellido, email=email)
            vendedor.save()

            return render(request, 'index.html')


    else:
        vendedorFormulario = VendedorFormulario()

    return render(request, 'crear_vendedor.html', {"vendedorFormulario": vendedorFormulario} )

def clientes(request):
    return render(request,'clientes.html')

def productos(request):
    return render(request, 'productos.html')

def ventas(request):
    return render(request, 'ventas.html')



def venta_formulario(request):
    if request.method == "POST":

        formulario = VentaFormulario(request.POST) 

        # print("formulario")
        # print(formulario)

        print(f"is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data

            nombre = datos.get("producto")
            cantidad = datos.get("cantidad")
            

            producto = Producto(nombre=nombre, cantidad=cantidad,)
            producto.save()

            return render(request, 'index.html')
        
    else:
        formulario = VentaFormulario()

    
    return render(request, 'venta_formulario.html', {"formulario": formulario})

def nuevo_vendedor(request):
    if request.method == "POST":

        formulario = NuevoVendedor(request.POST) 

        # print("formulario")
        # print(formulario)

        print(f"is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data

            
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            email = datos.get("email")

            vendedor = Vendedor(nombre=nombre, apellido=apellido, email=email)
            vendedor.save()

            return render(request, 'index.html')
        
    else:
        formulario = NuevoVendedor()

    
    return render(request, 'nuevo_vendedor.html', {"formulario": formulario})

@login_required
def nuevo_cliente(request):
    if request.method == "POST":

        formulario = NuevoCliente(request.POST) 

        # print("formulario")
        # print(formulario)

        print(f"is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data

            
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            email = datos.get("email")

            cliente = Cliente(nombre=nombre, apellido=apellido, email=email)
            cliente.save()

            return render(request, 'index.html')
        
    else:
        formulario = NuevoCliente()

    
    return render(request, 'nuevo_cliente.html', {"formulario": formulario})



@login_required   
def leer_vendedores(request):
    vendedores = Vendedor.objects.all()
    contexto = {"vendedores": vendedores}
    return render(request, 'leer_vendedores.html', contexto)
@login_required
def eliminar_vendedor(request, nombre_vendedor):
    
    vendedor = Vendedor.objects.get(nombre=nombre_vendedor)

    vendedor.delete()

    vendedores = Vendedor.objects.all()
    contexto = {"vendedores": vendedores}

    return render(request, 'leer_vendedores.html', contexto)
# vistas basadas en clases para el modelo Productos



class ProductoList(ListView):
 model = Producto
 template_name = 'producto_list.html'


class ProductoDetalle(DetailView):
 model = Producto
 template_name = 'producto_detalle.html'

class ProductoCreacion(LoginRequiredMixin, CreateView):
 model = Producto
 fields = ['nombre', 'cantidad']
 template_name = 'producto_form.html'
 success_url = "/coder-app/producto/list"

class ProductoUpdate(LoginRequiredMixin, UpdateView):
     model = Producto
     fields = ['nombre', 'cantidad']
     template_name = 'producto_form.html'
     success_url = "/coder-app/producto/list"
 
class ProductoDelete(LoginRequiredMixin, DeleteView):
     model = Producto
     template_name = 'producto_confirm_delete.html'
     success_url = "/coder-app/producto/list"

@login_required
def editar_vendedor(request, nombre_vendedor):
    vendedor = Vendedor.objects.get(nombre=nombre_vendedor)

    if request.method == "POST":
        formulario = VendedorFormulario(request.POST)

        if formulario.is_valid():
            datos_vendedor = formulario.cleaned_data

            vendedor.nombre = datos_vendedor.get("nombre")

            vendedor.apellido = datos_vendedor.get("apellido")
            vendedor.email = datos_vendedor.get("email")


            vendedor.save()
            return render(request, 'index.html')

    formulario = VendedorFormulario(initial={"nombre": vendedor.nombre, "apellido": vendedor.apellido, "email": vendedor.email})


    return render (request, "editar_vendedor.html", {"formulario": formulario, "vendedor_nombre": nombre_vendedor})

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"})
            else:
                return render(request, 'index.html', {"mensaje": f"Usuario o contraseña invalidos"})
            
        else:
            return render(request, "index.html", {"mensaje":"datos incorrectos"})
            


    form = AuthenticationForm

    return render(request, "login.html", {"form": form})

# def registrar(request):

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)

#         if form.is_valid():

#             username = form.cleaned_data.get("username")

#             form.save()
#         else:
#             print(form.errors)

#         return render(request, "index.html", {"mensaje": f"se dio alta el usuario {username}"})
#     form = UserCreationForm()
#     return render(request, "registro.html", {"form": form})

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def registrar(request):
    username = None  # Inicializa username fuera del bloque if

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "index.html", {"mensaje": f"se dio alta el usuario {username}"})
       

    form = UserCreationForm()
    return render(request, "registro.html", {"form": form})

@login_required
def avatar(request):

    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            user = User.objects.get(username = request.user)
            avatar = Avatar(user=user, image=formulario.cleaned_data.get("image"))
            avatar.save()

            return render(request, 'index.html')


    formulario = AvatarFormulario()

    return render(request, 'avatar.html', {"formulario": formulario} )


@login_required 
def leer_cliente(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes}
    return render(request, 'leer_clientes.html', contexto)



    