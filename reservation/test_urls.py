from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    reservation,
    MyBookingsView,
    OnlineBookingView,
    EditBookingView,
    DeleteBookingView,
)

class UrlsTest(SimpleTestCase):

    def test_reservation_url(self):
        url = reverse('reservation')
        self.assertEqual(resolve(url).func, reservation)

    def test_mybookings_url(self):
        url = reverse('mybookings')
        self.assertEqual(resolve(url).func.view_class, MyBookingsView)

    def test_online_booking_url(self):
        url = reverse('online_booking')
        self.assertEqual(resolve(url).func.view_class, OnlineBookingView)

    def test_edit_booking_url(self):
        booking_id = 1
        url = reverse('edit_booking', args=[booking_id])
        self.assertEqual(resolve(url).func.view_class, EditBookingView)

    def test_delete_booking_url(self):
        booking_id = 1
        url = reverse('delete_booking', args=[booking_id])
        self.assertEqual(resolve(url).func.view_class, DeleteBookingView)