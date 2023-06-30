from django import forms
from .models import No_of_guest, OnlineBooking


class OnlineBookingForm(forms.ModelForm):
    class Meta:
        model = OnlineBooking
        fields = (
            'first_name', 'last_name', 'no_of_guest',
            'reservation_datetime', 'time', 'occassion',
            'table', 'special_request'
            )
