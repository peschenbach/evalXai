from rest_framework import serializers
from .models import Prediction, Score


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['pk', 'prediction']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['pk', 'score']
