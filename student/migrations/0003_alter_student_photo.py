# Generated by Django 5.1.5 on 2025-02-02 16:22

import student.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to=student.models.student_photo_path),
        ),
    ]
