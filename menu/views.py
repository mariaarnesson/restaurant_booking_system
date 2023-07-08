from django.shortcuts import render
from .models import Menu, Meal, Drink


def menu(request):
    menus = Menu.objects.all()
    print(len(menus))
    return render(request, 'menu.html', {'menus': menus})
