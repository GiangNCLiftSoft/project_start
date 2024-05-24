from django.db import models



class Tag(models.Model):
    name=models.CharField(null=False,unique=True, max_length=50)

class Course(models.Model):
    name=models.CharField(max_length=100, null=False)
    price=models.FloatField()
    description=models.CharField(max_length=100,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    tag=models.ManyToManyField(Tag)


class Lesson(models.Model):
    name=models.CharField(max_length=20)
    time=models.FloatField()
    course=models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE )
    



    