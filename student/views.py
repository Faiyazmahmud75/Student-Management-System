from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.
def student(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        department = request.POST.get('department')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        photo = request.FILES.get('photo')

        student = models.Student(name=name, roll=roll, department=department, email=email, phone=phone, photo=photo)
        
        student.save()
        return HttpResponse('Student added successfully')

    return render(request, 'student/form.html')

def all_students(request):
    students = models.Student.objects.all()
    return render(request, 'student/allStudents.html', {'students': students})