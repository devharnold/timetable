from django.shortcuts import render
from rest_framework import viewsets # handles API views
from .models import Course, Lecturer, Timetable, Student #import models from the current app
from .serializers import CourseSerializer, TimetableSerializer, LecturerSeralizer, StudentSerializer #import corresponding serializer

# viewsets will define the behaviour of API endpoints
# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    #This API endpoint allows courses to be viewed or edited, retrieve all course objects and convert to json
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    #API endpoint allows lecturers to be viewed or edited, retreive all lecturers objects and convert data to json
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSeralizer

class TimetableViewSet(viewsets.ModelViewSet):
    # API endpoint that allows timetables to be viewed or edited
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

class StudentViewSet(viewsets.ModelViewSet):
    #API endpoint that allows students to be viewed or edited
    queryset = Student.objects.all()
    serializer_class = TimetableSerializer
    

