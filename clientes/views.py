from django.shortcuts import render, get_object_or_404
from .models import Animal


def index(request):
    animais = Animal.objects.all()
    return render(request, 'clientes/index.html', {
        'animais': animais
    })


def ver_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'clientes/ver_cliente.html', {
        'animal': animal
    })
