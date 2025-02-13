from django.db import models

# Create your models here.
class Course(models.Model):
    """Course model class. Defines the table in the db"""
    name = models.CharField(max_length=225)
    code = models.CharField(max_length=10, unique=True)

class Lecturer(models.Model):
    """Lecturer model class. Defines the table in the db"""
    name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)

class Student(models.Model):
    """Student model class. Defines the table in the db"""
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Timetable(models.Model):
    """Timetable model class. Defines the table in the db"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="timetables")
    week_days = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()


    class Meta:
        unique_together = ('lecturer', 'week_days', 'start_time')