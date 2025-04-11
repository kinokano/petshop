from django.shortcuts import render, redirect
from api.models import *
from django.contrib.auth import logout

from django.http import JsonResponse
from datetime import datetime, date


def index(request):
    return render(request, 'user/index.html')


def reserva(request):
    horarios_possiveis = [
        "08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
        "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
        "14:00", "14:30", "15:00", "15:30", "16:00", "16:30",
        "17:00", "17:30", "18:00"
    ]

    # 🟡 Parte 1: requisição AJAX para horários disponíveis
    if request.method == "GET" and request.GET.get("data"):
        try:
            data = datetime.strptime(request.GET.get("data"), "%Y-%m-%d").date()
            agendamentos = Agenda.objects.filter(data=data)
            ocupados = [a.hora.strftime('%H:%M') for a in agendamentos]
            disponiveis = [h for h in horarios_possiveis if h not in ocupados]
            return JsonResponse({"horarios": disponiveis})
        except ValueError:
            return JsonResponse({"erro": "Data inválida"}, status=400)

    # 🟢 Parte 2: formulário enviado (POST)
    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        especie = request.POST.get("especie")
        nome_animal = request.POST.get("nome_animal")
        porte = request.POST.get("porte")
        data_str = request.POST.get("data")
        hora_str = request.POST.get("horario")

        # Validação: data não pode ser no passado
        data_agendamento = datetime.strptime(data_str, "%Y-%m-%d").date()
        if data_agendamento < date.today():
            return render(request, 'user/reserva.html', {
                "erro": "A data escolhida já passou. Selecione uma data futura."
            })

        # Aqui você pode adicionar validações de horário também, se quiser.

        # Criação do agendamento
        Agenda.objects.create(
            nomeCliente=nome,
            telefone=telefone,
            especiePet=especie,
            nomePet=nome_animal,
            portePet=porte,
            data=data_agendamento,
            hora=datetime.strptime(hora_str, "%H:%M").time(),
            status="Pendente "
        )


        return render(request, 'user/reserva.html', {
    'pendente': True,
    'cliente': nome,
    'pet': nome_animal,
})

    tipo_servico_predefinido = request.GET.get("tipo", "")

    return render(request, 'user/reserva.html', {
    'pendente': False,
    'tipo_selecionado': tipo_servico_predefinido,
})



def loginAdm(request):
    return render(request, 'adm/loginAdm.html')

def indexAdm(request):
    return render(request, 'adm/indexAdm.html')
