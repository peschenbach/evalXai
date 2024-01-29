from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .models import *
from .serializers import *
from .worker_utils import trigger_evaluation_script_inside_worker


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser])
def xai_list(request):

    if request.method == "GET":
        xai_list = XAI.objects.all()
        serializer = XAISerializer(xai_list, many=True)
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
@parser_classes([MultiPartParser])
def xai_detail(request, challenge_id):

    try:
        xai = XAI.objects.get(challenge_id=challenge_id)
    except XAI.DoesNotExist:
        return Response(status=status.HTTP_404)

    if request.method == "GET":
        serializer = XAISerializer(xai)
        return Response(serializer.data)

    elif request.method == "POST":
        input_file = request.FILES.get('file')

        if input_file is None:
            return Response({'error': f'error getting the input file'}, status=status.HTTP_400_BAD_REQUEST)

        file_contents = input_file.read().decode('utf-8')
        message = trigger_evaluation_script_inside_worker(file_contents)

        return Response({'message': message}, status=status.HTTP_200_OK)

        

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
        
@api_view(['GET'])
def dataset_detail(request, challenge_id):
    try:
        dataset = Dataset.objects.get(challenge_id=challenge_id)
    except Dataset.DoesNotExist:
        return Response(status=status.HTTP_404)

    serializer = DatasetSerializer(dataset)
    return Response(serializer.data)

        
@api_view(['GET'])
def ai_detail(request, challenge_id):
    try:
        ai = Dataset.objects.get(challenge_id=challenge_id)
    except AI.DoesNotExist:
        return Response(status=status.HTTP_404)

    serializer = ScoreSerializer(ai)
    return Response(serializer.data)