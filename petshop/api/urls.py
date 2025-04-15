from django.urls import path, include

from api.views.apiViews import *
from api.views.webViews import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('agenda', AgendaViewSet)

urlpatterns = [

    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/users/', User.as_view()),
    path('api/login/', Login.as_view()),

    path('reserva/', reserva, name='reserva'),
    path('loginAdm/', loginAdm, name='loginAdm'),
    path('indexAdm/', indexAdm, name='indexAdm'),
    path('agendamentos/', agendamentos, name='agendamentos'),
    path('clientes/', clientes, name='clientes'),
    path('relatorios/', relatorios, name='relatorios'),



]