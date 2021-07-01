from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SurveySerializer
