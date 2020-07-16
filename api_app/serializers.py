from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['survey', 'text_question', 'text_answer']


# class QuestionSerializer(serializers.Serializer):
#     survey = serializers.CharField()
#     text_question = serializers.CharField()
#     text_answer = serializers.CharField()
#
#     class Meta:
#         model = Question
#

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'title', 'description', 'data_start', 'data_stop']

# class SurveySerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=250)
#     description = serializers.CharField()
#     data_start = serializers.DateField()
#     data_stop = serializers.DateField()
#
#     class Meta:
#         model = Survey
