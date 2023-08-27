from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Coincide con la URL raíz
    path('about/', views.about),
    path('hello/<str:username>/', views.hello),  # Coincide con URL con un parámetro username
]

