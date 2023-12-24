from rest_framework import serializers
from .models import Photo, Song,Emotion,Book 


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image', )


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('emotion',)

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'name', 'type', 'link', 'singer', 'thumbnail', 'duration')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'genre', 'author', 'link', 'emotion', 'thumbnail', 'description')
