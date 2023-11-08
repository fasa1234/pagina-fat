from django.urls import path
from . import views

urlpatterns = [
    path('myapp/login_registro/', views.login_registro, name='login_registro'),
    path('myapp/inicio_jugueteria/', views.inicio_jugueteria, name='inicio_jugueteria'),
]





