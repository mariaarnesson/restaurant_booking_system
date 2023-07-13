from django.test import TestCase
from django.urls import reverse
from .models import Menu, Meal


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_url = reverse('menu')
        self.meal_menu_url = reverse('meal_menu')