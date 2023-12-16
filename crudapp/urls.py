from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name="login_page"),
    path('register/', views.register, name='register'),
    path('logout-view/', views.logout_view, name='logout_view'),
    path('view-students/', views.view_students, name='view_students'),
    path('add-student/', views.add_student, name='add_student'),
    path('update-student/<int:id>/', views.update_student, name='update_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
]