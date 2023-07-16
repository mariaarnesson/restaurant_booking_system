from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import MenuView, MealView


class TestMenuUrls(SimpleTestCase):

    def test_menu_url_resolves(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func.view_class, MenuView)

    def test_meal_menu_url_resolves(self):
        url = reverse('meal', args=[1])
        self.assertEquals(resolve(url).func.view_class, MealView)
