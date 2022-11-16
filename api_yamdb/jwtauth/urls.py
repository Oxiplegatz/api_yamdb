from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from jwtauth.serializers import NewUserSerializer
from jwtauth.views import RegisterUserViewSet

urlpatterns = [
    path(
        'token/',
        TokenObtainPairView.as_view(serializer=NewUserSerializer),
        name='token_obtain_pair'
    ),
    path('signup/', RegisterUserViewSet, name='signup'),
]
