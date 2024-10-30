from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from tryhello.models import Student
import datetime

def hello_world(request,name):
    #s1 = Student(name=name, age=10, dob=datetime.datetime.today())
    #s1.save()
    student_id = Student.objects.get(name=name)
    student_id.age22=199
    #student_id.save()
    print(f"Hello World {name}!! Your age is {type(student_id)}")
    return HttpResponse(f"Hello World {name}!! Your age is {type(student_id)}")
