from importlib.resources import path
from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return render(request,"kabodproApp/home.html")


    


def pagar(request):
    return render(request,"kabodproApp/pagar.html")

def historial(request):
    return render(request,"kabodproApp/historial.html")



def salir(request):
    return HttpResponse("Salir")


