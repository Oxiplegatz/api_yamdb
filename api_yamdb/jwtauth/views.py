from rest_framework import viewsets

from jwtauth.serializers import NewUserSerializer


class RegisterUserViewSet(viewsets.ModelViewSet):
    serializer_class = NewUserSerializer
    pass


class VerifyUserViewSet(viewsets.ModelViewSet):
    pass
