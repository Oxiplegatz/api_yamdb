from django.urls import include, path

from rest_framework import routers

from .views import GenreViewSet, CategoryViewSet, TitleViewSet

router = routers.DefaultRouter()
router.register(r'titles', TitleViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
