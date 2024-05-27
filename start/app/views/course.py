from django.shortcuts import render, redirect, get_object_or_404
from ..models import Course,Tag

def index(request):
    tag_ids = request.GET.getlist('tag_ids')
    if tag_ids:
        courses = Course.objects.filter(tag__id__in=tag_ids, is_deleted=False).distinct()
    else:
        courses = Course.objects.filter(is_deleted=False)
    tags = Tag.objects.all()
    return render(request, 'index.html', {'courses': courses, 'tags': tags, 'selected_tag_ids': tag_ids})
    # courses = Course.objects.filter(is_deleted=False)
    # tag=Tag.objects.all()
    # return render(request, 'index.html', {'tags':tag,'courses': courses})

def add_course(request):
    tag=Tag.objects.all()
    return render (request,'addcourse.html',{'tags':tag})

def add_new_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        tags = request.POST.getlist('tags')
        course = Course.objects.create(name=name, description=description, price=price)
        course.tag.set(tags)
        return redirect('index') 
    tag=Tag.objects.all()
    return render (request,'addcourse.html',{'tags':tag})

def add_edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.price = request.POST.get('price')
        tags = request.POST.getlist('tags')
        course.tag.set(tags)
        course.save()
        return redirect('index') 
    tag=Tag.objects.all()
    return render (request ,'editcourse.html', {'tags':tag,'course': course} )

def delete_course(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('index') 
 
