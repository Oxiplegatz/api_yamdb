from django.urls import include, path

from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet,
                    GenreViewSet, ReviewViewSet,
                    TitleViewSet)

router = routers.DefaultRouter()
router.register(r'titles', TitleViewSet)
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
