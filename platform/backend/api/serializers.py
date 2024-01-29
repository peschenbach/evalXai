from rest_framework import serializers
from .models import *

class XAISerializer(serializers.ModelSerializer):
    class Meta:
        model = XAI
        fields = ['xai']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['score']

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ['dataset']

class AISerializer(serializers.ModelSerializer):
    class Meta:
        model = AI
        fields = ['ai']