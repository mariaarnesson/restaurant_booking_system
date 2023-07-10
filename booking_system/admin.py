from django.contrib import admin
from .models import Customer, NumberPeople, AvailableTime, Reservation

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['your_name', 'your_email']

@admin.register(NumberPeople)
class NumberPeopleAdmin(admin.ModelAdmin):
    list_display = ['seats']

@admin.register(AvailableTime)
class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ['book_time']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['available_time', 'number_people', 'book_date', 'status', 'user']            
