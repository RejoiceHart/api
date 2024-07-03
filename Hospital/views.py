from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,  IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer, LoginSerializer

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    # queryset = User.objects.all()
    

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            hospital_name=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


