

from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    stu_user = models.CharField(max_length=40)
    stu_pass = models.CharField(max_length=40)  
    stu_marks = models.IntegerField(default=0)
    stu_marks_java = models.IntegerField(default=0)
    stu_marks_php = models.IntegerField(default=0)

class Subject(models.Model):
    subname = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.subname}"
    

class Question(models.Model):
    question = models.CharField(max_length=200)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
    Marks = models.IntegerField(default=1)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject}"  