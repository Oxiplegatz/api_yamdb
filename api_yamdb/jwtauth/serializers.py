from rest_framework import serializers

from users.models import CustomUser


class NewUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', )

    def create_user(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        user = CustomUser(username=username, email=email)
        user.save()
        # return CustomUser.email_user(subject, message)
