from django.db import models
import os

# Create your models here.
def student_photo_path(instance, filename):
    return os.path.join('student/media/', instance.name, filename)

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    department = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(default=None, null=True, upload_to=student_photo_path)

    def __str__(self):
        return f"{self.name}"
