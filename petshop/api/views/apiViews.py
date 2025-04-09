from rest_framework import viewsets, status
from api.models import *
from api.serializers import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

class User(APIView):
    def get(self, request, id=None):
        if id:
            usuario = get_object_or_404(CustomUser, pk=id)
            serializer = UserSerializer(usuario)
            return Response(serializer.data, status= status.HTTP_200_OK)

        usuario = CustomUser.objects.all()
        serializer = UserSerializer(usuario, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request):
        nome = request.data.get('nome')
        senha = request.data.get('senha')
        ra = request.data.get('ra')
        fistName = request.data.get('first_name')
        # isAdm = request.data.get('is_adm')
        
        if not nome or not senha:
            return Response({"error": "Todos os campos são obrigatórios!", "status": status.HTTP_400_BAD_REQUEST}, status= status.HTTP_400_BAD_REQUEST)

        usuario = CustomUser.objects.create(
            username = nome,
            password = make_password(senha),
            is_active = True,
            first_name = fistName,
            
            ra = ra
        )
        return Response({"message":"Usuário criado com sucesso!", "id":usuario.id, "status": status.HTTP_201_CREATED}, status= status.HTTP_201_CREATED)

    def put(self, request, id):
        usuario = get_object_or_404(CustomUser, pk=id)

        senha = request.data.get('password', None)

        if senha and usuario.password != senha: 
            request.data['password'] = make_password(senha)

        serializer = UserSerializer(usuario, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK})

        return Response(serializer.errors, {"status": status.HTTP_400_BAD_REQUEST})

    def delete(self, request, id):
        usuario = get_object_or_404(CustomUser, pk = id)
        if usuario:
            usuario.delete()
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"status": status.HTTP_404_NOT_FOUND})
        
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        usuario = authenticate(username=username, password=password)
    
        if(usuario):
            login(request, usuario)
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"mensagem": "Usuario nao encontrado!", "status": status.HTTP_401_UNAUTHORIZED})