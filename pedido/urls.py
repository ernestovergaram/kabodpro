from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedido, name="Pedido"),
]
