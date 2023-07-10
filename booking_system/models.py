from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Approved'),
    (2, 'Canceled'),
)

TIME_CHOICES = [
    ("10 AM - 12 AM", "10 AM - 12 AM"),
    ("11 AM - 1 PM", "11 AM - 1 PM"),
    ("12 PM - 2 PM", "12 PM - 2 PM"),
    ("1 PM - 3 PM", "1 PM - 3 PM"),
    ("2 PM - 4 PM", "2 PM - 4 PM"),
    ("3 PM - 5 PM", "3 PM - 5 PM"),
    ("4 PM - 6 PM", "4 PM - 6 PM"),
    ("5 PM - 7 PM", "5 PM - 7 PM"),
    ("6 PM - 8 PM", "6 PM - 8 PM"),
    ("7 PM - 9 PM", "7 PM - 9 PM"),
    ("8 PM - 10 PM", "8 PM - 10 PM"),
]

class Customer(models.Model):
    your_name = models.CharField(max_length=20, blank=False)
    your_email = models.EmailField()

    def __str__(self):
        return self.your_name


class NumberPeople(models.Model):
    seats = models.CharField(null=False, blank=False, max_length=60)

    def __str__(self):
        return str(self.seats)


class AvailableTime(models.Model):
    book_time = models.CharField(null=True, blank=False,
                            choices=TIME_CHOICES, max_length=60)

    def __str__(self):
        return str(self.book_time)


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    available_time = models.ForeignKey('AvailableTime', on_delete=models.CASCADE)
    number_people = models.ForeignKey('NumberPeople', on_delete=models.CASCADE)
   
    book_date = models.DateField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.number_people} on {self.book_date}"



