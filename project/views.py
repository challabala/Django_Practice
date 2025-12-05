from django.http import HttpResponse
from django.shortcuts import render
from app.models import Employee

def home(req):
    employees = Employee.objects.all()
    context = {
        'employees':employees,
    }
    return render(req,'home.html',context)