from django import forms
from .models import Student


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'address', 'student_class']

        widgets = { 'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'student_class': forms.TextInput(attrs={'class': 'form-control'}),
        }

