# Django Rest Framework
from rest_framework import serializers

# Local
from rest_framework.exceptions import PermissionDenied

from ecommerce.apps.users.models import User, UserSecession, UserAddress
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


class UserAddressSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('id', 'name', 'phone', 'main_address', 'sub_address', 'is_default')


class UserAddressCreateSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('name', 'phone', 'main_address', 'sub_address', 'postal_code', 'is_default')

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        validated_data['user'] = user
        delivery = UserAddress.objects.create(**validated_data)
        return delivery


class UserAddressUpdateSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('name', 'phone', 'main_address', 'sub_address', 'postal_code', 'is_default')

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if instance.user == user:
            instance.update(**validated_data)
            return instance
        raise PermissionDenied
