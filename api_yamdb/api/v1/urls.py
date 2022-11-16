from django.urls import include, path

from rest_framework import routers

from .views import GenreViewSet, CategoryViewSet, TitleViewSet

router = routers.DefaultRouter()
router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('genres/', GenreViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('genres/<slug:slug>/', GenreViewSet.as_view({'delete': 'destroy'})),
    path('categories/', CategoryViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('categories/<slug:slug>/', CategoryViewSet.as_view({
        'delete': 'destroy'
    })),
]
