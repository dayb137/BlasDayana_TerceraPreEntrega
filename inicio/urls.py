from django.urls import path
from inicio import views



urlpatterns = [
    path('', views.inicio),
    path('personas/crear/<str:nombre>/<str:apellido>/', views.crear_persona, name='crear_persona'),
    
]