from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            telefono=request.POST.get("telefono")
            contenido=request.POST.get("contenido")
            
            email=EmailMessage("mensaje",
            "El usuario con el nombre {} con la direccion {} escribe lo siguiente: \n\n {} y deja su numero de tlf {}" .format(nombre,email,contenido,telefono), "informaticaiute@gmail.com",['informaticaiute@gmail.com'])
            try:
                email.send
                return redirect("/contacto/?enviado")
            except:
                return redirect("/contacto/?noenviado")



    return render(request,"contacto/contacto.html",{'miformulario':formulario_contacto})
