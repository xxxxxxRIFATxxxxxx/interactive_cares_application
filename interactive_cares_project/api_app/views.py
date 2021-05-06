from course_app import models
from api_app import serializers
from rest_framework import viewsets, parsers

# Create your views here.
class CourseViewset(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
