from django.shortcuts import render
from .models import Movie, Director, Category
from rest_framework import viewsets, permissions, filters
from .serializers import MovieSerializer, DirectorSerializer, CategorySerializer
from .permissions import UserPermission

# Create your views here.

class DirectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows directors to be viewed or edited.
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [permissions.IsAuthenticated,UserPermission,]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated,UserPermission,]


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    search_fields = ['name', 'director__first_name', 'director__last_name', 'genre__title', 'popularity','imdb_score']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.IsAuthenticated,UserPermission,]