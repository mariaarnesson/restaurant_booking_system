from django import forms


class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')


class DateForm(forms.Form):
    date = forms.DateField(
        label='Date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )