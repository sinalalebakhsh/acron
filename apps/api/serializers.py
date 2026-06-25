# apps/api/serializers.py

from rest_framework import serializers


from apps.accounts import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser

        fields = ['id', 'username', 'email', 'first_name', 'last_name',]

