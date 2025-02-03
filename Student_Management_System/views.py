from django.shortcuts import render
from student import models

def home(request):
    students = models.Student.objects.all()
    for student in students:
        if not student.photo:
            student.photo_url = '/static/images/default-photo.jpg'
        else:
            student.photo_url = student.photo.url
    return render(request, 'index.html', {'students': students})