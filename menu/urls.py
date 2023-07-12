from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuView.as_view(), name='menu'),
    path('meal/<int:pk>/', views.MealView.as_view(), name='meal'),
]