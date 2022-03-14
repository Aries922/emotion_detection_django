import json
import uuid
from io import BytesIO

from django.http import HttpResponse
from django.core import serializers
from rest_framework.generics import ListAPIView
from .models import Photo, Emotion, Song, Conditions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework import status
from django.core.files.storage import default_storage
from fer import FER
import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
from numpy import asarray
from PIL import Image as PImage
import cv2
import json

import os

from django.conf import settings

from .serializers import ImageSerializer, EmotionSerializer






def detect_faces(image_path):
    image = PImage.open(default_storage.open(image_path))
    image = image.convert('RGB')
    pixels = asarray(image)

    detector = MTCNN()

    results = detector.detect_faces(pixels)

    detected_faces = list()
    for result in results:

        if result['confidence'] > 0.90:
            detected_faces.append({
                "face_id": uuid.uuid4(),
                "confidence": result['confidence'],
                "bounding_box": result['box'],
                "keypoints": result['keypoints']
            })

    return detected_faces


class ImageViewSet(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = ImageSerializer


    def post(self, request, *args, **kwargs):

        file = request.data['image']
        print(file)
        Photo.objects.create(image=file)
        obj = Photo.objects.all().last() 
        image = obj.image

        detector = FER(mtcnn=True)
        img = plt.imread(settings.MEDIA_ROOT+"/"+image.name)

        detect_faces = detector.detect_emotions(img)
        obj.delete();
        
        return Response({"success": detect_faces}, status=status.HTTP_202_ACCEPTED)



class EmotionViewSet(ListAPIView):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer


    def post(self, request, *args, **kwargs):
        typed = ""; 
        string = request.data['emotion']
        conditions = Conditions.objects.filter(condition = string);
        if(len(conditions) == 0):
            typed = string;
        else:
            typed = conditions[0].type;
        songs = Song.objects.filter(type = typed);
        songs = serializers.serialize('json', songs);   
        print(songs)
        
        return Response(songs, status=status.HTTP_202_ACCEPTED)


class ConditionViewSet(ListAPIView):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer


    def post(self, request, *args, **kwargs):

        string = request.data['emotion']
        print(string);
        conditions = Conditions.objects.filter(type = string);
        conditions = serializers.serialize('json', conditions);   
        print(conditions)
        
        return Response(conditions, status=status.HTTP_202_ACCEPTED)