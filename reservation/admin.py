from django.contrib import admin
from .models import No_of_guest, OnlineBooking


class No_of_guestAdmin(admin.ModelAdmin):
    list_display = ('guest',)


class OnlineBookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'no_of_guest', 'reservation_datetime', 'approved')
    list_filter = ('approved', 'reservation_datetime')
    search_fields = ('first_name', 'last_name')
    date_hierarchy = 'reservation_datetime'


admin.site.register(No_of_guest, No_of_guestAdmin)
admin.site.register(OnlineBooking, OnlineBookingAdmin)
