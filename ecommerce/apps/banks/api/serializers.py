# Local
from ecommerce.apps.banks.models import BankAccount
from ecommerce.bases.api.serializers import ModelSerializer


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('id', 'user', 'bank', 'account', 'name')


class BankAccountCreateSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('bank', 'account', 'name')

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        validated_data['user'] = user
        bank_account = BankAccount.objects.create(**validated_data)
        return bank_account
