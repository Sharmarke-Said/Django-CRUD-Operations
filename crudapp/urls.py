from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-student/', views.add_student, name='add_student'),
    # Add other URL patterns as needed
]