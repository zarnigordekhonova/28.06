from django.shortcuts import render
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from .serializers import CreateUserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(['POST'])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(password=password, username=username)
    if user:
        auth_token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": auth_token.key}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": "You logged out."}, status=status.HTTP_200_OK)


