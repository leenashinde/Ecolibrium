from .models import Movie, Director, Category
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director_name = serializers.SerializerMethodField('get_director_name')
    genre = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id','name','popularity','director','director_name','imdb_score','genre')

    def get_director_name(self, obj):
        return '{} {}'.format(obj.director.first_name,obj.director.last_name)