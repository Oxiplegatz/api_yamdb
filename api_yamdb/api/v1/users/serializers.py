from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'username': {'required': True},
        }

    def validate_role(self, value):
        if value not in ['user', 'admin', 'moderator']:
            raise ValidationError(
                'Невозможно назначить пользователю такую роль.'
            )
        return value


class CasualUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )
        read_only_fields = ('role', )
