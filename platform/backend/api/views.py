from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .worker_utils import trigger_evaluation_script_inside_worker
from django.shortcuts import get_object_or_404


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
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def prediction_detail(request, user_id):

    try:
        prediction = Prediction.objects.get(pk=user_id)
    except Prediction.DoesNotExist:
        prediction = None
        return Response(status=status.HTTP_404)

    if request.method == "GET":
        if prediction:
            serializer = PredictionSerializer(prediction)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404)

    elif request.method == "POST":
        serializer = PredictionSerializer(
            data=request.data, instance=prediction)
        if serializer.is_valid():
            serializer.save()
            trigger_evaluation_script_inside_worker()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Print validation errors to the console for debugging
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def score_detail(request, user_id):

    try:
        score = Score.objects.get(pk=user_id)
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404)

    if request.method == "GET":
        score = get_object_or_404(Score, pk=user_id)
        serializer = ScoreSerializer(score)
        return Response(serializer.data)

    # if request.method == "POST":
    #     serializer = ScoreSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         # Print validation errors to the console for debugging
    #         print(serializer.errors)
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "POST":
        score = get_object_or_404(Score, pk=user_id)
        serializer = ScoreSerializer(data=request.data, instance=score)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Print validation errors to the console for debugging
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
