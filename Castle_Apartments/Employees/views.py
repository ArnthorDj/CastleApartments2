from django.shortcuts import render


def employees(request):
    return render(request, 'Employees/employees.html')