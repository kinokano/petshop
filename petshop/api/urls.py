from django.urls import path, include

from api.views.apiViews import *
from api.views.webViews import *
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('', index, name='index'),
    path('reserva/', reserva, name='reserva')

]