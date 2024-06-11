from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'detail': 'Username already exists'})
    user = User.objects.create_user(username=username, password=password)
    return Response({'detail': 'User created'})

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'detail': 'Logged in'})
    else:
        return Response({'detail': 'Invalid credentials'})

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'detail': 'Logged out'})