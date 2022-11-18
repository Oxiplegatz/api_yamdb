from django.urls import path

from api.v1.jwtauth.views import SignUpView, obtain_token

urlpatterns = [
    path('token/', obtain_token, name='obtain_token'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
