from django.shortcuts import render
from django.views import View
from .models import OnlineBooking
from .forms import OnlineBookingForm
from datetime import date
from django.contrib import messages


def reservation(request):
    return render(request, "reservation.html", {})


class OnlineBookingView(View):

    total_tables = 30
    booked_tables = OnlineBooking.objects.count()

    def get(self, request):
        available_tables = self.total_tables - self.booked_tables
        form = OnlineBookingForm()
        context = {
            'form': form,
            'available_tables': available_tables,
        }
        return render(request, 'online_booking.html', context)

      def post(self, request):

        form = OnlineBookingForm(request.POST)

        if request.user.is_authenticated:
            
            if form.is_valid():
                reservation = form.save(commit=False)
                if reservation.date < date.today():
                    messages.error(request, 'You cannot book a table for a past date.')
                    return redirect('online_booking')

                reservation.user = request.user
                reservation.approved = False
                reservation.save()
                request.session['online_booking_id'] = reservation.id
                messages.success(request, 'Reservation request submitted successfully. Your booking is pending approval.')
                return redirect('mybookings')
            else:
                messages.error(request, 'The table is already booked.')
        else:
            messages.error(request, 'You need to log in to make a booking.')        

            context = {
                'form': form,
            }
            return render(request, 'online_booking.html', context)    
