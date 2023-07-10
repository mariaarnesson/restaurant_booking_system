from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_a_table, name='book_a_table'),
]