from django.test import TestCase
from django.contrib.auth.models import User
from .models import No_of_guest, OnlineBooking


class ModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
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

    def test_no_of_guest_model(self):
        self.assertEqual(str(self.no_of_guest), '2')

    def test_online_booking_model(self):
        self.assertEqual(str(self.booking.date), '2023-07-13')
        self.assertEqual(str(self.booking.user), 'testuser')
        self.assertEqual(self.booking.approved, False)
