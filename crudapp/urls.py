from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-student/', views.add_student, name='add_student'),
    path('update-student/<int:id>/', views.update_student, name='update_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
]