from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import OnlineBooking, No_of_guest
from .forms import OnlineBookingForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime, date
from django.db.models import Q


def reservation(request):
    return render(request, "reservation.html", {})


class MyBookingsView(View):
    """
    Summary of the table reservation with the data provided
    in the form and confirmation of the status.
    """
    template_name = 'mybookings.html'

    def get(self, request):
        if request.user.is_authenticated:
            online_bookings = (
                OnlineBooking.objects
                .filter(user=request.user)
                .order_by('date')
            )
            context = {
                'online_bookings': online_bookings,
            }
            return render(request, 'mybookings.html', context)
        else:
            messages.error(
                request,
                'You need to log in to view your bookings.'
            )
            return redirect('login')


class OnlineBookingView(View):
    template_name = 'online_booking.html'
    total_tables = 10
    max_bookings_per_day = 10

    def get_available_slots(self, date):

        available_slots = []

        for time_choice, _ in OnlineBooking.TIME_CHOICES:
            time = time_choice
            booked_tables = (
                OnlineBooking.objects
                .filter(date=date, time=time)
                .count()
            )
            remaining_slots = self.total_tables - booked_tables
            if remaining_slots > 0:
                available_slots.append((time, remaining_slots))

        return available_slots

    def get(self, request):

        current_date = datetime.now().date()
        form = OnlineBookingForm()
        available_slots = []

        for time_choice in OnlineBooking.TIME_CHOICES:
            time = time_choice[0]
            booked_tables = OnlineBooking.objects.filter(date=current_date,
                                                         time=time).count()
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

                if reservation.date < date.today():
                    messages.error(
                        request,
                        'You cannot book a table for a past date.'
                    )
                    return redirect('online_booking')

                booked_tables_on_reservation_date = (
                    OnlineBooking.objects
                    .filter(date=reservation.date, time=reservation.time)
                    .count()
                )

                if (booked_tables_on_reservation_date >=
                        self.max_bookings_per_day):
                    messages.error(
                        request,
                        'No more tables available for'
                        ' the selected date and time.'
                    )
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
                messages.success(
                    request,
                    'Reservation request submitted successfully.'
                    'Your booking is pending approval.'
                )
                return redirect('mybookings')
            else:
                messages.error(request, 'Error in filling out the form.')
        else:
            messages.error(request, 'You need to log in to make a booking.')

        context = {
            'form': form,
        }
        return render(request, 'online_booking.html', context)


class EditBookingView(View):

    template_name = 'edit_booking.html'
    total_tables = 10
    max_bookings_per_day = 10

    def get_available_slots(self, date):
        booked_tables = OnlineBooking.objects.filter(date=date).count()
        available_slots = []

        for time_choice, _ in OnlineBooking.TIME_CHOICES:
            time = time_choice
            remaining_slots = self.total_tables - booked_tables
            if remaining_slots > 0:
                available_slots.append((time, remaining_slots))
                booked_tables -= 1

        return available_slots

    def get(self, request, booking_id):
        booking = get_object_or_404(
            OnlineBooking,
            id=booking_id,
            user=request.user
        )
        form = OnlineBookingForm(instance=booking)
        context = {
            'form': form,
        }
        return render(request, 'edit_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(
            OnlineBooking,
            id=booking_id,
            user=request.user
        )
        form = OnlineBookingForm(request.POST, instance=booking)

        if form.is_valid():
            reservation = form.save(commit=False)
            if reservation.date < date.today():
                messages.error(
                    request,
                    'You cannot book a table for a past date.'
                )
                return redirect('online_booking')

            booked_tables_on_reservation_date = (
                OnlineBooking.objects
                .filter(date=reservation.date, time=reservation.time)
                .exclude(id=booking_id)
                .count()
            )

            if booked_tables_on_reservation_date >= self.max_bookings_per_day:
                messages.error(
                    request,
                    'No more tables available for the selected date and time.'
                )
                return redirect('online_booking')

            reservation.user = request.user
            reservation.approved = False
            form.save()
            request.session['online_booking_id'] = reservation.id
            messages.success(
                request,
                'Booking updated successfully.'
                'Your booking is pending approval.'
            )
            return redirect('mybookings')
        else:
            messages.error(request, 'The table is already booked.')

        context = {
            'form': form,
        }
        return render(request, 'edit_booking.html', context)


class DeleteBookingView(View):
    template_name = 'delete_booking.html'

    def get(self, request, booking_id):
        booking = get_object_or_404(
            OnlineBooking,
            id=booking_id,
            user=request.user
        )
        context = {
            'booking': booking,
        }
        return render(request, 'delete_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(
            OnlineBooking,
            id=booking_id,
            user=request.user
        )
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('mybookings')
