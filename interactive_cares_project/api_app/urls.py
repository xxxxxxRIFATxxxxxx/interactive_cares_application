from django.urls import path
from api_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f"courses", views.CourseViewset, basename="courses")

urlpatterns = [] + router.urls
