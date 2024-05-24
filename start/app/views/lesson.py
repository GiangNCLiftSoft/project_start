from django.shortcuts import render,get_object_or_404
from ..models import Lesson, Course

def add_lesson_page(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'addlesson.html',{'course':course})

def add_list_lesson(request,course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        names = request.POST.getlist('name')
        times = request.POST.getlist('time')
        for name, time in zip(names, times):
            lesson = Lesson(name=name, time=time, course=course)
            lesson.save()
        
    return render(request, 'index.html')


 
