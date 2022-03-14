from rest_framework import serializers
from .models import Photo,Emotion, Song,Conditions


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image', )


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('emotion',)

