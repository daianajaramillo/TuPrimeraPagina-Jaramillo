from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alojamiento-form/', views.form_alojamiento, name='form_alojamiento'),
    path('anfitrion-form/', views.form_anfitrion, name='form_anfitrion'),
    path('reserva-form/', views.form_reserva, name='form_reserva'),
    path('buscar-alojamiento/', views.buscar_alojamiento, name='buscar_alojamiento'),
]