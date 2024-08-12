from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User as DjangoUser
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if DjangoUser.objects.filter(username=username).exists():
            return Response({'success': False, 'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if DjangoUser.objects.filter(email=email).exists():
            return Response({'success': False, 'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = DjangoUser.objects.create_user(username=username, email=email, password=password)

        if user is not None:
            return Response({'success': True, 'message': 'User created successfully', 'user_id': user.id})
        else:
            return Response({'success': False, 'message': 'Failed to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'success': True, 'message': 'Login successful', 'user_id': user.id})
        else:
            return Response({'success': False, 'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)



class LogoutUser(APIView):
    def post(self, request):
        logout(request)
        return Response({'success': True, 'message': 'Logout successful'})
