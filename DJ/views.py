from django.http import HttpResponse
from django.shortcuts import render

from employees.apps import EmployeesConfig
from employees.models import Employee

def home(request):
    """Home Method"""
    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request, 'home.html', context)