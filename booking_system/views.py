from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import BookingForm, DateForm
from .models import AvailableTime, Reservation
from django.views import View


def book_a_table(request):
    return render(request, "book_a_table.html", {})


class ChooseDateView(View):
    def get(self, request):
        date_form = DateForm()
        return render(request, 'choose_date.html', {'date_form': date_form})    
