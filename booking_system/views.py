from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import BookingForm, DateForm
from .models import AvailableTime, Reservation
from django.views import View


def book_a_table(request):
    return render(request, "book_a_table.html", {})


class ChooseDateView(View):
    template_name = 'choose_date.html'
    form_class = DateForm
    success_url = '/select-time/'


class SelectTimeView(View):
    template_name = 'select_time.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.request.GET.get('date')
        available_times = AvailableTime.objects.filter(date=date)
        context['available_times'] = available_times
        return context

    def post(self, request, *args, **kwargs):
        time_slot = request.POST.get('time_slot')
        request.session['time_slot'] = time_slot
        return redirect('contact_details')