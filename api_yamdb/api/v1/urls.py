from django.urls import include, path

from rest_framework import routers

from .views import GenreViewSet, CategoryViewSet, TitleViewSet

router = routers.DefaultRouter()
router.register(r'titles', TitleViewSet)
router.register(r'^genres/(?P<slug>[-\w]*)$', GenreViewSet, basename='genres')
router.register(
    r'^categories/(?P<slug>[-\w]*)$', CategoryViewSet, basename='categories'
)

urlpatterns = [
    path('', include(router.urls)),
]
