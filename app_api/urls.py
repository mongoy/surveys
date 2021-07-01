from rest_framework import routers
from .api import SurveyViewSet


router = routers.DefaultRouter()
router.register('api/survey', SurveyViewSet, 'survey')


urlpatterns = router.urls
