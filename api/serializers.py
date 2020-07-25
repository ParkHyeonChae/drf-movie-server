"""api/serializers.py"""

from rest_framework import serializers
from .models import MovieList


# JSON 변환을 위한 Serializers
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = ['title', 'year', 'rating', 'genre', 'summary']