from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Approved'),
    (2, 'Canceled'),
)


class Customer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    your_name = models.CharField(max_length=20, blank=False)
    your_email = models.EmailField()

    def __str__(self):
        return self.your_name


class NumberPeople(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    seats = models.IntegerField(null=False, blank=False)
    min_people = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return str(self.seats)


class AvailableTime(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    book_time = models.CharField(max_length=20, null=False, blank=False)

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



