from django import forms
from .models import No_of_guest, OnlineBooking


class OnlineBookingForm(forms.ModelForm):
    class Meta:
        model = OnlineBooking
        fields = (
            'first_name', 'last_name', 'no_of_guest',
            'date', 'occassion',
            'table', 'special_request'
            )
        exclude = ["user"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }    
"""
    def get_available_dates(self):
        booked_dates = OnlineBooking.objects.values_list('date', flat=True)

        today = date.today()
        end_date = today + timedelta(days=30)
        available_dates = [today + timedelta(days=i) for i in range((end_date - today).days)]

        available_dates = [date for date in available_dates if date not in booked_dates]

        return available_dates
"""        