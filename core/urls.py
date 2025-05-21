from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),

    # Add below student URLs
path('teachers/', views.teacher_list, name='teacher_list'),
path('teachers/add/', views.add_teacher, name='add_teacher'),
path('teachers/edit/<int:pk>/', views.edit_teacher, name='edit_teacher'),
path('teachers/delete/<int:pk>/', views.delete_teacher, name='delete_teacher'),

]
