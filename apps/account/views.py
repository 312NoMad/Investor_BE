from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from django.contrib.auth import get_user_model

from .models import CustomUser as User
from .serializers import UserSignUpSerializer, UserSerializer


__all__ = [
    'SignInView',
    'SignUpView',
    'SignOutView',
    'RefreshTokenView',
    'CurrentUserView',
]


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name']
            )
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(TokenObtainPairView):
    permission_classes = [AllowAny]


class SignOutView(TokenBlacklistView):
    pass


class RefreshTokenView(TokenRefreshView):
    pass


class CurrentUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.queryset.get(id=request.user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
