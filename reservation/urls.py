from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('online_booking/', views.OnlineBookingView.as_view(), name='online_booking'),
    path('mybookings/', views.MyBookingsView.as_view(), name='mybookings'),
    path('edit_booking/<int:booking_id>/', views.EditBookingView.as_view(), name='edit_booking'),
]