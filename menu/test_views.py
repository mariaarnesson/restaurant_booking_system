from django.test import TestCase, Client
from django.urls import reverse
from .models import Menu, Meal


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_url = reverse('menu')

    def test_menu_get_context_data(self):
        response = self.client.get(self.menu_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
