from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, OrderViewSet, CustomerViewSet, ReviewViewSet, AuthorViewSet, GenreViewSet, PublisherViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]