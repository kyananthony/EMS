from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from EMS.settings.models import Employee
from static_my_project.forms import EmployeeForm

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully.')
            return redirect('view_employees')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/view_employees.html', {'employees': employees})

def update_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('view_employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('view_employees')
    return render(request, 'employees/delete_employee.html', {'employee': employee})
