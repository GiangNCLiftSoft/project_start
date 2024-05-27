from django.urls import path
from . import views
urlpatterns = [
    path('',views.course.index,name="index"),

    path('course/add/', views.course.add_new_course, name='add_new_course'),
    path('course/update/<int:course_id>', views.course.add_edit_course, name='add_edit'),  
    path('course/delete/<int:course_id>/', views.course.delete_course, name='delete_course'),
   
    path('course/addlistlesson/<int:course_id>',views.lesson.add_list_lesson,name="add_list_lesson"),

    path('lesson/delete/<int:course_id>', views.lesson.delete_lessons,name='delete_lessons'),
    path('lesson/update/<int:course_id>/<int:lesson_id>', views.lesson.update_lesson,name='update_lessons'),
    path('lesson/<int:course_id>',views.lesson.lessons,name="view_list_lesson"),

    path('tags/', views.tag.tag_list, name='tag_list'),
    path('tags/add/', views.tag.add_tag, name='add_tag'),
    path('tags/delete/<int:tag_id>/', views.tag.delete_tag, name='delete_tag'),
]