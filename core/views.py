from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


from .models import Teacher
from .forms import TeacherForm

# List all teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'core/teacher_list.html', {'teachers': teachers})

# Add a teacher
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'core/teacher_form.html', {'form': form, 'action': 'Add'})

# Edit a teacher
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'core/teacher_form.html', {'form': form, 'action': 'Edit'})

# Delete a teacher
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'core/teacher_confirm_delete.html', {'teacher': teacher})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form, 'action': 'Add'})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form, 'action': 'Edit'})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/student_confirm_delete.html', {'student': student})
