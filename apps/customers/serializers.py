from rest_framework import serializers

from .models import Customer

from apps.accounts import models as accounts_models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = accounts_models.CustomUser

        fields = [
            'id',
            'username',
            'email',
        ]




class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Customer

        fields = [
            'id',
            'uuid',
            'phone_number',
            'birth_date',
            'user',
        ]
        read_only_fields = [
            'id',
            'uuid',
            'user',
        ]






