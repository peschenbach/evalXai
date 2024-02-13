from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .models import *
from .serializers import *
from .worker_utils import trigger_evaluation_script_inside_worker
from django.http import HttpResponse


@api_view(['POST'])
@parser_classes([MultiPartParser])
def xai_detail(request, challenge_id):

    input_file = request.FILES.get('file')

    if input_file is None:
        return Response({'error': f'error getting the input file'}, status=status.HTTP_400_BAD_REQUEST)

    file_contents = input_file.read().decode('utf-8')
    message = trigger_evaluation_script_inside_worker(
        file_contents, challenge_id)

    return Response({'message': message}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def score_detail(request, challenge_id):

    try:
        score = Score.objects.filter(challenge_id=challenge_id).first()
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404)

    if request.method == "GET":
        serializer = ScoreSerializer(score)
        return Response(serializer.data)

    if request.method == "POST":
        if score:  # If a score with this challenge_id already exists
            serializer = ScoreSerializer(score, data=request.data)
        else:
            # Create a new score if it doesn't exist
            serializer = ScoreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def dataset_detail(request, challenge_id):
    # try:
    #     dataset = Dataset.objects.get(challenge_id=challenge_id)
    # except Dataset.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # serializer = DatasetSerializer(dataset)
    # return Response(serializer.data)
    file_path = "./dataset/train_data.pt"

    try:
        with open(file_path, 'rb') as file:
            data = file.read()
    except Exception as e:
        return Response({'error': f'Error reading file: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Set the content type to application/octet-stream to indicate a binary file
    response = HttpResponse(data, content_type='application/octet-stream')

    # Set the file name in the Content-Disposition header
    response['Content-Disposition'] = f'attachment; filename="train_data.pt"'

    return response


@api_view(['GET'])
def ai_detail(request, challenge_id):
    # try:
    #     model = Mlmodel.objects.get(challenge_id=challenge_id)
    # except Mlmodel.DoesNotExist:
    #     return Response(status=status.HTTP_404)

    # serializer = MlmodelSerializer(model)
    # return Response(serializer.data)

    file_path = "./ml_model/cnn.pt"

    try:
        with open(file_path, 'rb') as file:
            data = file.read()
    except Exception as e:
        return Response({'error': f'Error reading file: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Set the content type to application/octet-stream to indicate a binary file
    response = HttpResponse(data, content_type='application/octet-stream')

    # Set the file name in the Content-Disposition header
    response['Content-Disposition'] = f'attachment; filename="cnn.pt"'

    return response
