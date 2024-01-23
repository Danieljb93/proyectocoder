from django import forms


class VentaFormulario(forms.Form):
    producto = forms.CharField(max_length=20, required=False)
    cantidad = forms.IntegerField()


class NuevoVendedor(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()

class NuevoCliente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()

class VendedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class AvatarFormulario(forms.Form):
    image = forms.ImageField()


