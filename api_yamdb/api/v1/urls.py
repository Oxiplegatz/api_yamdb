from django.urls import include, path

from rest_framework import routers

<<<<<<< HEAD
from .views import (CategoryViewSet, CommentViewSet,
                    GenreViewSet, ReviewViewSet,
                    TitleViewSet)
=======
from api.v1.users.views import UserViewSet
from api.v1.reviews.views import (CategoryViewSet, CommentViewSet,
                                  GenreViewSet, ReviewViewSet,
                                  TitleViewSet)
>>>>>>> 38dd4e4cb21aa9ea8f04f8218c380671d4e77bd3

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'titles', TitleViewSet)
<<<<<<< HEAD
=======
router.register(r'genres', GenreViewSet)
router.register(r'categories', CategoryViewSet)
>>>>>>> 38dd4e4cb21aa9ea8f04f8218c380671d4e77bd3
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('auth/', include('api.v1.jwtauth.urls')),
    path('', include(router.urls)),
]
