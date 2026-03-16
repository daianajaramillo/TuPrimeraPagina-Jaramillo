from django.shortcuts import render

# Create your views here.
from .models import Alojamiento, Anfitrion, Reserva
from .forms import AlojamientoForm, AnfitrionForm, ReservaForm

def inicio(request):
    lista_alojamientos = Alojamiento.objects.all()
    return render(request, "mi_app/index.html", {"alojamientos": lista_alojamientos})

#Views para Forms
def form_alojamiento(request):
    if request.method == "POST":
        formulario = AlojamientoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nuevo = Alojamiento(
                nombre=info['nombre'],
                ciudad=info['ciudad'],
                precio_por_noche=info['precio_por_noche'],
                capacidad_personas=info['capacidad_personas']
            )
            nuevo.save()
            return render(request, "mi_app/index.html", {"mensaje": "Alojamiento guardado correctamente"})
    else:
        formulario = AlojamientoForm()
    return render(request, "mi_app/form_alojamiento.html", {"mi_form": formulario, "titulo": "Cargar Alojamiento"})

def form_anfitrion(request):
    if request.method == "POST":
        formulario = AnfitrionForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nuevo = Anfitrion(
                nombre=info['nombre'],
                apellido=info['apellido'],
                email=info['email'],
                telefono=info['telefono'],
                idiomas=info['idiomas']
            )
            nuevo.save()
            return render(request, "mi_app/index.html", {"mensaje": "Anfitrión guardado correctamente"})
    else:
        formulario = AnfitrionForm()
    return render(request, "mi_app/form_anfitrion.html", {"mi_form": formulario, "titulo": "Cargar Anfitrión"})

def form_reserva(request):
    if request.method == "POST":
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nuevo = Reserva(
                nombre_viajero=info['nombre_viajero'],
                fecha_inicio=info['fecha_inicio'],
                fecha_fin=info['fecha_fin'],
                cantidad_huespedes=info['cantidad_huespedes'],

            )
            nuevo.save()
            return render(request, "mi_app/index.html", {"mensaje": "Reserva guardada correctamente"})
    else:
        formulario = ReservaForm()
    return render(request, "mi_app/form_reserva.html", {"mi_form": formulario, "titulo": "Cargar Reserva"})

# View para Form wue busca en BD
def buscar_alojamiento(request):
    ciudad_buscada = request.GET.get("ciudad")
    
    if ciudad_buscada:
        resultados = Alojamiento.objects.filter(ciudad__icontains=ciudad_buscada)
        return render(request, "mi_app/buscar_alojamiento.html", {
            "alojamientos": resultados, 
            "ciudad": ciudad_buscada,
            "busqueda_realizada": True
        })
    
    return render(request, "mi_app/buscar_alojamiento.html", {"busqueda_realizada": False})