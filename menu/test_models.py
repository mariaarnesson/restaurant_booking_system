from django.test import TestCase
from django.urls import reverse
from .models import Menu, Meal


class MenuModelTest(TestCase):

    def test_str_representation(self):
        menu = Menu(title='Sample Menu')
        self.assertEqual(str(menu), 'Sample Menu')


class MealModelTest(TestCase):

    def test_str_representation(self):
        meal = Meal(mealName='Sample Meal')
        self.assertEqual(str(meal), 'Sample Meal')
