# Django Rest Framework
from rest_framework import serializers

# Local
from ecommerce.apps.users.models import User, UserSecession
from ecommerce.bases.api.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'phone')


class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class TokenSerializer(ModelSerializer):
    token = serializers.CharField(source='auth_token')

    class Meta:
        model = User
        fields = ('token',)


class WithdrawSerializer(ModelSerializer):
    class Meta:
        model = UserSecession
        fields = ('reason',)
