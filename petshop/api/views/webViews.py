from django.shortcuts import render, redirect
from api.models import *
from django.contrib.auth import logout


def index(request):
    return render(request, 'user/index.html')

def reserva(request):
    return render(request, 'user/reserva.html')