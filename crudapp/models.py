from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    student_class = models.CharField(max_length=255)
    student_image = models.ImageField(null=True, blank=True, upload_to='student_images/')
    def __str__(self) -> str:
        return f"{self.name} - {self.email} - {self.address} - {self.student_class}"
