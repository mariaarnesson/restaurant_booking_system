from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'mealName', 'price')
    search_fields = ('title', 'mealName')


admin.site.register(Menu, MenuAdmin)
