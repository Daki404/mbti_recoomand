from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers


class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lectures
        fields = '__all__'