from django.urls import path
from . import views


urlpatterns = [
    path('menu', views.menu_view, name='menu'),
    path('meal/<int:menu_id>/', views.meal_view, name='meal'),
]