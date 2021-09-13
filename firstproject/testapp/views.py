from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import employee
# Create your views here.
def employee_info(request):
    employees=employee.objects.all()
    data={'employees':employees}
    return render(request,'testapp/employees.html',data)
def greeting(request):
    s={'x':"heello contains"}
    return render(request,'testapp/greeting.html',s)
def showContact(request):
    s="<h1>contact page</h1>"
    s+="<p>Website:music.com</p>"
    s+="<p>Mobile:9878978687</p>"
    return HttpResponse(s)
def about(request):
    s="<h1> This is an about page</h1>"
    return HttpResponse(s)
