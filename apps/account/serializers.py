from rest_framework import serializers

from .models import CustomUser as User


__all__ = [
    'UserSerializer',
    'UserSignUpSerializer'
]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
