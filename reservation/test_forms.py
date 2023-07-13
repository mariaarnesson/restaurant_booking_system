from django.test import TestCase
from datetime import date, timedelta
from .forms import OnlineBookingForm


class FormsTest(TestCase):

    def test_online_booking_form_get_available_dates(self):
        form = OnlineBookingForm()
        available_dates = form.get_available_dates()

        self.assertIsInstance(available_dates, list)

        for date_obj in available_dates:
            self.assertIsInstance(date_obj, date)
