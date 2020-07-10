from django.shortcuts import render,redirect
from .forms import Eployeeform
from .models import Employee

def employee_list(request):
    context = {'Employee_list': Employee.objects.all()}
    return render(request, 'eployee_app/List.html', context)

def employee_form(request,id=0):
    if request.method == 'GET':
        if id==0:
           form  =  Eployeeform()
        else:
            employee = Employee.objects.get(pk=id)
            form = Eployeeform(instance=employee)
        return  render(request,'eployee_app/Form.html',{'form':form})
    else:
        if id == 0:
          form = Eployeeform(request.POST)
        else:
          employee = Employee.objects.get(pk=id)
          form = Eployeeform(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('forlist')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('forlist')