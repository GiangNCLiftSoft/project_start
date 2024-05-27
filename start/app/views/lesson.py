from django.shortcuts import render,get_object_or_404,redirect
from ..models import Lesson, Course


def add_list_lesson(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        names = request.POST.getlist('name')
        times = request.POST.getlist('time')
        for name, time in zip(names, times):
            lesson = Lesson(name=name, time=time, course=course)
            lesson.save()
        return redirect('index')
    return render(request, 'addlesson.html',{'course':course})


def lessons(request, course_id):
    course = get_object_or_404(Course, pk=course_id, is_deleted=False)
    lessons = Lesson.objects.filter(course=course, is_deleted=False)
    return render(request, 'lessons.html', {'course': course, 'lessons': lessons})

def update_lesson(request,course_id, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    course = get_object_or_404(Course, pk=course_id, is_deleted=False)
    if request.method == 'POST':
        lesson.name = request.POST.get('name')
        lesson.time = request.POST.get('time')
        lesson.save()
        return  redirect('view_list_lesson', course_id=course_id)
    return render(request, 'editlesson.html', {'course': course, 'lesson': lesson})

def delete_lessons(request, course_id):
    course = get_object_or_404(Course, pk=course_id, is_deleted=False)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete_selected':
            lesson_ids = request.POST.getlist('lesson_ids[]')
            Lesson.objects.filter(id__in=lesson_ids, course=course).update(is_deleted=True)
        elif action == 'delete_all':
            Lesson.objects.filter(course=course).update(is_deleted=True)
    return redirect('view_list_lesson', course_id=course_id)