from django.shortcuts import render,redirect

from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def emp(request):
    if request.method == "POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('employee:show')
            except:
                pass
    else:
        form = EmployeeForm()

    return render(request, 'index.html',{'form':form})
    
def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html',{'employee':employee})

def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee:show')
    return render(request, 'edit.html', {'employee':employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee:show')
      
