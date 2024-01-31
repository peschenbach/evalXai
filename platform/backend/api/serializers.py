from rest_framework import serializers
from .models import *


class XAISerializer(serializers.ModelSerializer):
    class Meta:
        model = XAI
        fields = ["challenge_id", 'xai']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["challenge_id", 'score']


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ["challenge_id","dataset", 'data']


class AISerializer(serializers.ModelSerializer):
    class Meta:
        model = AIModel
        fields = ["challenge_id", 'ai_model']
