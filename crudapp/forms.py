
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student


class CreateUserForm(UserCreationForm):

    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'address', 'student_class', 'student_image']

        widgets = { 'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'student_class': forms.TextInput(attrs={'class': 'form-control'}),
                   'student_image': forms.ClearableFileInput(attrs={'class': 'form-control'})

        }

