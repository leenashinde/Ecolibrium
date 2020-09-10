from django.urls import path,include
from .views import DirectorViewSet, CategoryViewSet, MovieViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'directors', DirectorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
