from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, CreateUserForm
from .models import Student

# Create your views here.



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



@login_required(login_url='login_page')
def register(request):
    if request.user.is_authenticated:
        return redirect('view_students')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login_page')
            
        return render(request, 'crudapp/register.html', {'form': form})




def login_page(request):
    if request.user.is_authenticated:
        return redirect('view_students')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('view_students')  # Update the view name to your desired view
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login_page')

        return render(request, 'crudapp/login.html')


def logout_view(request):
    logout(request)
    return redirect('login_page')



    


        # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # return redirect('view_students')
    # else:
    #     form = UserCreationForm()




@login_required(login_url='login_page')
def view_students(request):
    students = Student.objects.all()
    form = StudentRegistrationForm()  # Create an empty form
    return render(request, 'crudapp/index.html', {'students': students, 'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentRegistrationForm()

    # students = Student.objects.all()  # Add this line to fetch all students
    return render(request, 'crudapp/index.html', {'form': form})



def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

        return redirect('view_students')
    
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

        return redirect('view_students')
    # else:
    #     form = StudentRegistrationForm()


    return render(request, 'crudapp/update_student.html',
                   {'form': form, 
                    'student': student})