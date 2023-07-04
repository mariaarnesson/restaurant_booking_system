from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import OnlineBooking
from .forms import OnlineBookingForm
from datetime import date
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse


def reservation(request):
    return render(request, "reservation.html", {})


class MyBookingsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            online_bookings = OnlineBooking.objects.filter(user=request.user)
            context = {
                'online_bookings': online_bookings,
            }
            return render(request, 'mybookings.html', context)
        else:
            messages.error(request, 'You need to log in to view your bookings.')
            return redirect('login')


class OnlineBookingView(View):
    total_tables = 10
    max_bookings_per_day = 10
    
    def get(self, request):
        current_date = datetime.now().date()
        form = OnlineBookingForm()
        available_slots = []

        for time_choice in OnlineBooking.TIME_CHOICES:
            time = time_choice[0]
            booked_tables = OnlineBooking.objects.filter(date=current_date, time=time).count()
            remaining_slots = self.total_tables - booked_tables
            if remaining_slots > 0:
                available_slots.append((time, remaining_slots))


        context = {
            'form': form,
            'available_slots': available_slots,
        }
        return render(request, 'online_booking.html', context)

    def post(self, request):

        form = OnlineBookingForm(request.POST)

        if request.user.is_authenticated:
            
            if form.is_valid():
                reservation = form.save(commit=False)
                if reservation.date < datetime.now().date():
                    messages.error(request, 'You cannot book a table for a past date.')
                    return redirect('online_booking')

                current_date = datetime.now().date()
                booked_tables_today = OnlineBooking.objects.filter(date=current_date).count()    

                if reservation.date == current_date and booked_tables_today >= self.max_bookings_per_day:
                    messages.error(request, 'No more tables available for today. Please choose another date.')
                    return redirect('online_booking')

                available_slots = self.get_available_slots(reservation.date)

                context = {
                    'form': form,
                    'available_slots': available_slots,
                }    

                reservation.user = request.user
                reservation.approved = False
                reservation.save()
                request.session['online_booking_id'] = reservation.id
                messages.success(request, 'Reservation request submitted successfully. Your booking is pending approval.')
                return redirect('mybookings')
            else:
                messages.error(request, 'Error in filling out the form.')
        else:
            messages.error(request, 'You need to log in to make a booking.')        

        context = {
                'form': form,
                
        }
        response = render(request, 'online_booking.html', context)
        return HttpResponse(response.content)


class EditBookingView(View):

    def get(self, request, booking_id):
        booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)
        form = OnlineBookingForm(instance=booking)
        context = {
            'form': form,
        }
        return render(request, 'edit_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)
        form = OnlineBookingForm(request.POST, instance=booking)

        if form.is_valid():
            reservation = form.save(commit=False)
            if reservation.date < date.today():
                messages.error(request, 'You cannot book a table for a past date.')
                return redirect('online_booking')

            reservation.user = request.user
            reservation.approved = False
            form.save()
            request.session['online_booking_id'] = reservation.id
            messages.success(request, 'Booking updated successfully. Your booking is pending approval.')
            return redirect('mybookings')
        else:
            messages.error(request, 'The table is already booked.')

        context = {
            'form': form,
        }
        return render(request, 'edit_booking.html', context)


class DeleteBookingView(View):

    def get(self, request, booking_id):
        booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)
        context = {
            'booking': booking,
        }
        return render(request, 'delete_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(OnlineBooking, id=booking_id, user=request.user)
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('mybookings')        

