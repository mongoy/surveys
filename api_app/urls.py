from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SurveyList, SurveyDetail  # surveys_list, surveys_detail


urlpatterns = [
    # path('api/surveys-list/<int:pk>/', surveys_detail, name='surveys-detail'),
    # path('api/surveys-list/', surveys_list, name='surveys-list'),
    path('api/surveys-list/<int:pk>/', SurveyDetail.as_view(), name='surveys-detail'),
    path('api/surveys-list/', SurveyList.as_view(), name='surveys-list'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
