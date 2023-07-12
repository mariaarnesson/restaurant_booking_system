from django.shortcuts import render, get_object_or_404
from .models import Menu, Meal


def menu_view(request):
    menus = Menu.objects.all()
    print(len(menus))
    return render(request, 'menu.html', {'menus': menus})


def meal_view(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    menus = Menu.objects.all() 
    meals = menu.meal_set.all()
    return render(request, 'meal.html', {'menu': menu, 'menus': menus, 'meals': meals})

