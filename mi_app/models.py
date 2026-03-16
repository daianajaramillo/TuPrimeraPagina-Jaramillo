from django.db import models

# Create your models here.

from django.db import models

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    precio_por_noche = models.IntegerField()
    capacidad_personas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"

class Anfitrion(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    idiomas = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.idiomas})"

class Reserva(models.Model):
    nombre_viajero = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_huespedes = models.IntegerField(default=1)

    def __str__(self):
        return f"Reserva de {self.nombre_viajero}"
