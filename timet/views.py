from django.shortcuts import render
from rest_framework import viewsets
from .models import Course, Lecturer, Timetable, Student
from .serializers import CourseSerializer, TimetableSerializer, LecturerSeralizer, StudentSerializer

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSeralizer

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = TimetableSerializer
    

