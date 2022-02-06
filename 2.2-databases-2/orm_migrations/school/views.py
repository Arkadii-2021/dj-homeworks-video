from django.views.generic import ListView
from django.shortcuts import render
from .models import Teacher, Student


def students_list(request):
    template = 'school/students_list.html'
    student = Student.objects.all()
    teachers = Teacher.objects.all()
    for student_list in student:
        print(f'\n{student_list.name}, класс: {student_list.group}')
        print('\tПреподаватели:')
        for teacher_list in student_list.teachers.all():
            print(f'\t{teacher_list.name}, предмет: {teacher_list.subject}')
    context = {
        'object_list': student,
        'teachers': teachers,
    }
    return render(request, template, context)
