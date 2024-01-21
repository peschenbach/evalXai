from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .models import *
from .serializers import *
from .worker_utils import trigger_evaluation_script_inside_worker


@api_view(['GET', 'POST'])
@parser_classes([FileUploadParser])
def prediction_list(request):

    if request.method == "GET":
        predictions = Prediction.objects.all()
        serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        input_file = request.FILES.get('file')

        if input_file is None:
            return Response({'error': f'error getting the input file'}, status=status.HTTP_400_BAD_REQUEST)

        file_contents = input_file.read().decode('utf-8')
        message = trigger_evaluation_script_inside_worker(file_contents)

        return Response({'message': message}, status=status.HTTP_200_OK)

        # serializer = PredictionSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     # TODO: spawn container and run evaluate.py
        #     # before spawning, get the network name as a parameter,
        #     # and connect the new container to it.
        #     trigger_evaluation_script_inside_worker()
        #     return Response(data=serializer.data, status = status.HTTP_201_CREATED)


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