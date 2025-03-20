#urls will be used incase we decide to develop the user interface of the app
# use djangorest framework
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LecturerViewSet, StudentViewSet, TimetableViewSet

router = DefaultRouter() # defaultRouter automatic generates url patterns for API views incase we use Viewsets
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lecturer', LecturerViewSet)
router.register(r'timetables', TimetableViewSet)

url_pattern = [
    path('api/', include(router.urls))
]