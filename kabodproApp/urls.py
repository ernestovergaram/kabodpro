from django.urls import path
from kabodproApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.Home, name="Home"),
 
    
    path('pagar/', views.pagar, name="Pagar"),
    path('historial/', views.historial, name="Historial"),
  
    path('salir/', views.salir, name="Salir"),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)