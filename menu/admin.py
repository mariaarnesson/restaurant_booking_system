from django.contrib import admin
from .models import Menu, Meal


class MealInline(admin.TabularInline):
    model = Meal


class MenuAdmin(admin.ModelAdmin):
    inlines = [MealInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Meal)

