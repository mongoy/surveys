import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Survey
from .serializers import SurveySerializer


d_today = datetime.date.today()


@api_view(['GET', 'POST'])
def surveys_list(request, format=None):
    """
    Все актуальные опросы и создание новых
    :param format:
    :param request:
    :return:
    """
    if request.method == 'GET':
        surveys = Survey.objects.all().filter(data_stop__gte=d_today, data_start__lte=d_today)
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)  # возврат данных

    elif request.method == 'POST':
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def surveys_detail(request, pk, format=None):
    """
    Извлечение, обновление или удаление кода.
    """
    try:
        surveys = Survey.objects.get(pk=pk)
    except Survey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SurveySerializer(surveys)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SurveySerializer(surveys, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        surveys.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
