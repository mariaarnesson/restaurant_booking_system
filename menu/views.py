from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Menu, Meal


class MenuView(generic.ListView):
    template_name = 'menu.html'
    context_object_name = 'menus'
    queryset = Menu.objects.all()


class MealView(generic.DetailView):
    template_name = 'meal.html'
    model = Menu
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        context['meals'] = self.object.meal_set.all()
        return context
