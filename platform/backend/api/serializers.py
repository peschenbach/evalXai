from rest_framework import serializers
from .models import *


class XaimethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xaimethod
        fields = ["challenge_id", "xai_method"]


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["challenge_id", "score"]


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ["challenge_id", "dataset", "data"]


class MlmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mlmodel
        fields = ["challenge_id", 'model']
