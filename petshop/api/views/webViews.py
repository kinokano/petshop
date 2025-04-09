from django.shortcuts import render, redirect
from api.models import *
from django.contrib.auth import logout


def index(request):
    return render(request, 'user/index.html')

def reserva(request):
    horarios = [
        "08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
        "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
        "14:00", "14:30", "15:00", "15:30", "16:00", "16:30",
        "17:00", "17:30", "18:00"
    ]
    return render(request, 'user/reserva.html', {'horarios': horarios})



def loginAdm(request):
    return render(request, 'adm/loginAdm.html')

def indexAdm(request):
    return render(request, 'adm/indexAdm.html')