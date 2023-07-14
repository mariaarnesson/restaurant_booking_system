from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .views import (
    MyBookingsView,
    OnlineBookingView,
    EditBookingView,
    DeleteBookingView,
)
from .models import OnlineBooking, No_of_guest


class ViewsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.no_of_guest = No_of_guest.objects.create(guest=2)
        self.booking = OnlineBooking.objects.create(
            user=self.user,
            first_name='Maria',
            last_name='Arnesson',
            no_of_guest=self.no_of_guest,
            date='2023-07-13',
            time='10 AM - 12 AM',
            occassion='Birthday',
            table='Family table',
            special_request='Some special request',
            approved=False,
        )

    def test_my_bookings_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('mybookings'))
        self.assertEqual(response.status_code, 200)

    def test_my_bookings_view_unauthenticated(self):
        response = self.client.get(reverse('mybookings'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')

    def test_online_booking_view_get(self):
        response = self.client.get(reverse('online_booking'))
        self.assertEqual(response.status_code, 200)

    def test_online_booking_view_post(self):
        data = {
            'first_name': 'Maria',
            'last_name': 'Arnesson',
            'no_of_guest': self.no_of_guest.id,
            'date': '2023-07-13',
            'time': '10 AM - 12 AM',
            'occassion': 'Birthday',
            'table': 'Family table',
            'special_request': 'Some special request',
        }
        response = self.client.post(reverse('online_booking'), data)
        print(response.content.decode())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mybookings/')

    def test_edit_booking_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('edit_booking', args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_edit_booking_view_post(self):
        self.client.force_login(self.user)
        data = {
            'first_name': 'Maria',
            'last_name': 'Arnesson',
            'no_of_guest': self.no_of_guest.id,
            'date': '2023-07-13',
            'time': '10 AM - 12 AM',
            'occassion': 'Birthday',
            'table': 'Family table',
            'special_request': 'Some special request',
        }
        response = self.client.post(
            reverse('edit_booking', args=[self.booking.id]), data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mybookings/')

    def test_delete_booking_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('delete_booking', args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_booking_view_post(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('delete_booking', args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/mybookings/')
