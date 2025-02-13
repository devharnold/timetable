from django.contrib import admin
from .models import Course, Student, Lecturer, Timetable

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Timetable)
