import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from .models import Survey
from .serializers import SurveySerializer


d_today = datetime.date.today()


class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all().filter(data_stop__gte=d_today, data_start__lte=d_today)
    serializer_class = SurveySerializer

# class SurveyList(APIView):
#     """
#
#     """
#     def get(self, request, format=None):
#         surveys = Survey.objects.all().filter(data_stop__gte=d_today, data_start__lte=d_today)
#         serializer = SurveySerializer(surveys, many=True)
#         return Response(serializer.data)  # возврат данных
#
#     def post(self, request, format=None):
#         serializer = SurveySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def surveys_list(request, format=None):
#     """
#     Все актуальные опросы и создание новых
#     :param format:
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         surveys = Survey.objects.all().filter(data_stop__gte=d_today, data_start__lte=d_today)
#         serializer = SurveySerializer(surveys, many=True)
#         return Response(serializer.data)  # возврат данных
#
#     elif request.method == 'POST':
#         serializer = SurveySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all().filter(data_stop__gte=d_today, data_start__lte=d_today)
    serializer_class = SurveySerializer

# class SurveyDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Survey.objects.get(pk=pk)
#         except Survey.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         surveys = self.get_object(pk)
#         serializer = SurveySerializer(surveys)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         surveys = self.get_object(pk)
#         serializer = SurveySerializer(surveys, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         surveys = self.get_object(pk)
#         surveys.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def surveys_detail(request, pk, format=None):
#     """
#     Извлечение, обновление или удаление кода.
#     """
#     try:
#         surveys = Survey.objects.get(pk=pk)
#     except Survey.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SurveySerializer(surveys)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SurveySerializer(surveys, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         surveys.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
