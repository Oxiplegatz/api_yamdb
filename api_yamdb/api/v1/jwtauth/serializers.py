from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', )
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'username': {'required': True},
        }

    def validate_username(self, value):
        if value == 'me':
            raise ValidationError('Выбранное имя пользователя недоступно.')
        return value


class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    confirmation_code = serializers.CharField(max_length=8, required=True)
