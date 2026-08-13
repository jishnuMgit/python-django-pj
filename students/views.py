from django.shortcuts import render
from django.http import HttpResponse
def students(request):
    students=[
        {
        'id':1,'name':'jishnu','age':22
    }
    ]
    return HttpResponse(students)