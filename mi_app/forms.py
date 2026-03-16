from django import forms

class AlojamientoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)
    precio_por_noche = forms.IntegerField()
    capacidad_personas = forms.IntegerField()

class AnfitrionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    idiomas = forms.CharField(max_length=100)

class ReservaForm(forms.Form):
    nombre_viajero = forms.CharField(max_length=100)
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget)
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget)
    cantidad_huespedes = forms.IntegerField(initial=1)

#Form para buscar en BD
class BuscarAlojamientoForm(forms.Form):
    ciudad = forms.CharField(max_length=100)