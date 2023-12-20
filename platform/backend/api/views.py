from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def prediction_list(request):

    if request.method == "GET":
        predictions = Prediction.objects.all()
        serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # TODO: spawn container and run evaluate.py
            # before spawning, get the network name as a parameter,
            # and connect the new container to it.
            return Response(data=serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def prediction_detail(request, id):

    try:
        prediction = Prediction.objects.get(pk=id)
    except Prediction.DoesNotExist:
        return Response(status=status.HTTP_404)

    if request.method == "GET":
        serializer = PredictionSerializer(prediction)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'POST'])
def score_list(request):

    if request.method == "GET":
        scores = Score.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def score_detail(request, id):

    try:
        score = Score.objects.get(pk=id)
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404)

    if request.method == "GET":
        serializer = ScoreSerializer(score)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status = status.HTTP_201_CREATED)