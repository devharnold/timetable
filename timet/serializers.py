#serializer file

"""
used `serializers.ModelSerializer` because it auto-generates fields
and is way much more easier to use.
It works directly with django models, automatically generates fields from the model
"""

from rest_framework import serializers
from .models import Course, Timetable, Lecturer, Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' # include all fields from the model

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'

    
    def prevent_conflict(self, data):
        #We want to prevent collision therefore we first fetch existing data
        details = Timetable.objects.filter(
            lecturer = data['lecturer'],
            week_day = data['week_day']
        ).exclude(id=self.instance.id if self.instance else None) # exclude instance ids, just pick lecturer and the particular day of the week

        for entry in details:
            if (data['start_time'] < entry.end_time and data['end_time'] > entry.start_time):
                raise serializers.ValidationError("Lecturer assigned a class at this time of the day!")
            
        return data

