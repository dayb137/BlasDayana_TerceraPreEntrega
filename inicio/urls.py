from django.urls import path
from inicio import views



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('personas/crear/', views.crear_persona, name='crear_persona'),
    path('personas/', views.personas, name='ver_persona'),
]