from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import StudentRegistrationForm
from .models import Student

# Create your views here.


def index(request):
    students = Student.objects.all()
    form = StudentRegistrationForm()  # Create an empty form
    return render(request, 'crudapp/index.html', {'students': students, 'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentRegistrationForm()

    # students = Student.objects.all()  # Add this line to fetch all students
    return render(request, 'crudapp/index.html', {'form': form})



def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

        return redirect('index')
    
    return render(request, 'crudapp/index.html', {'student': student})


# def update_student(request, id):
#     student = get_object_or_404(Student, id=id)

#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # Redirect to the home page after a successful update

#     else:
#         form = StudentRegistrationForm(instance=student)

#     return render(request, 'crudapp/index.html', {'student': student})

# def update_student(request, id):
#     student = get_object_or_404(Student, id=id)

#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = StudentRegistrationForm(instance=student)
    
#     return render(request, 'crudapp/index.html', {'form': form, 'student': student})


# def update_student(request, id):
#     # For debugging purpose
#     print('ID: ', id) 
#     student = get_object_or_404(Student, id=id)

#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = StudentRegistrationForm(instance=student)

#     # for debugging purpose
#     print(student)
    
#     return render(request, 'crudapp/index.html', {'form': form, 'student': student})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentRegistrationForm(instance=student)

    # Fetch all students for the table
    students = Student.objects.all()
    return render(request, 'crudapp/index.html', {'form': form, 'student': student, 'students': students})