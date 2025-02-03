from django.shortcuts import render, redirect
from . import models

# Create your views here.
def create_student(request):
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
        return redirect('home')

    return render(request, 'student/form.html')

def update_student(request, id):
    student = models.Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll = request.POST.get('roll')
        student.department = request.POST.get('department')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.photo = student.photo
        
        if request.FILES.get('photo'):
            student.photo = request.FILES.get('photo')

        student.save()
        return redirect('home')

    return render(request, 'student/form.html', {'student': student, 'update': True})

def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return redirect('home')