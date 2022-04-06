from django.shortcuts import render
from .models import Company, Employee, Library

def home(request):
    employees = Employee.objects.all().select_related('company')

    for employee in employees:
        print(employee.name)

def home2(request):
    employees = Employee.objects.all()

    for employee in employees:
        print(employee.library_set.all())
    return None
