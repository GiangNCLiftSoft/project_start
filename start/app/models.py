from django.db import models

class Tag(models.Model):
    name=models.CharField(null=False,unique=True, max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField()
    description = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super(Course, self).delete(*args, **kwargs)

class Lesson(models.Model):
    name = models.CharField(max_length=20)
    time = models.FloatField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super(Course, self).delete(*args, **kwargs)
    