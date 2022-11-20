from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser
from api.v1.users.permissions import IsAdmin, IsOwner
from api.v1.users.serializers import UserSerializer, CasualUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdmin, )
    lookup_field = 'username'

    @action(methods=['get', 'patch'], permission_classes=[IsOwner],
            detail=False, url_path='me')
    def get_me(self, request):
        if not request.user.is_authenticated:
            return Response(
                'Пожалуйста, авторизуйтесь.', status.HTTP_401_UNAUTHORIZED
            )
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        if user.role == 'user':
            serializer = CasualUserSerializer(
                user, data=request.data, partial=True
            )
        else:
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
