from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'crudapp/index.html')

def add_student(request):
    return render(request, 'crudapp/students.html')
