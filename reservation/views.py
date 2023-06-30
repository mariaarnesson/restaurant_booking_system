from django.shortcuts import render
from django.views import View


def reservation(request):
    return render(request, "reservation.html", {})
