from django.shortcuts import render, redirect, get_object_or_404
from ..models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def add_course(request):
    return render (request,'addcourse.html')

def reder_edit_course(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render (request ,'editcourse.html', {'course': course} )

def add_new_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Course.objects.create(name=name, description=description, price=price)
        return redirect('index') 
    return render(request, 'index.html') 

def add_edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.price = request.POST.get('price')
        course.save()
        return redirect('index') 
    return render(request, 'edit_course.html', {'course': course})

def delete_course(course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('index') 
 
