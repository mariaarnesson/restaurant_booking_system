from django.contrib import admin
from .models import Menu, Meal, Drink


class MealInline(admin.TabularInline):
    model = Meal


class DrinkInline(admin.TabularInline):
    model = Drink    


class MenuAdmin(admin.ModelAdmin):
    inlines = [MealInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Meal)
admin.site.register(Drink)
