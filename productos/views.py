from django.shortcuts import render
from productos.models import Producto
# Create your views here.
def producto(request):
    producto=Producto.objects.all()
    return render(request,"productos/producto.html", {"producto":producto})