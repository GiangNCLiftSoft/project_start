from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.course.index,name="index"),
    path('add/', views.course.add_course, name='add_course'),
    path('add_new_course/', views.course.add_new_course, name='add_new_course'),
    path('edit/<int:course_id>', views.course.reder_edit_course, name='edit_course_page'),
    path('editcourse/<int:course_id>', views.course.add_edit_course, name='add_edit'),  
    path('delete/<int:course_id>/', views.course.delete_course, name='delete_course'),
    path('add_lesson/<int:course_id>', views.lesson.add_lesson_page, name="add_lessons" ) ,
    path('addlistlesson/',views.lesson.add_list_lesson,name="add_list_lesson"),

]