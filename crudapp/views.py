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
        form = StudentRegistrationForm(request.POST, request.FILES)
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
#         form = StudentRegistrationForm(request.POST or None, request.FILES or None, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = StudentRegistrationForm(instance=student)

#     return render(request, 'crudapp/index.html', {'form': form, 'student': student})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    # if request.method == 'POST':
    form = StudentRegistrationForm(request.POST or None, request.FILES or None, instance=student)

    if form.is_valid():
        form.save()

        return redirect('index')
    # else:
    #     form = StudentRegistrationForm()


    return render(request, 'crudapp/update_student.html',
                   {'form': form, 
                    'student': student})