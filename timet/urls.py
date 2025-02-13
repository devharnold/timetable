from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LecturerViewSet, StudentViewSet, TimetableViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lecturer', LecturerViewSet)
router.register(r'timetables', TimetableViewSet)

url_pattern = [
    path('api/', include(router.urls))
]