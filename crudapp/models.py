from django.db import models
import os
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    student_class = models.CharField(max_length=255)
    student_image = models.ImageField(null=True, blank=True, upload_to='student_images/')

    def __str__(self) -> str:
        return f"{self.name} - {self.email} - {self.address} - {self.student_class}"


    def save(self, *args, **kwargs):
        # Check if the object already exists in the database
        if self.pk is not None:
            # Retrieve the existing object
            existing_student = Student.objects.get(pk=self.pk)
            # Check if the existing object has an image
            if existing_student.student_image:
                # Delete the existing image file
                os.remove(existing_student.student_image.path)

        super().save(*args, **kwargs)