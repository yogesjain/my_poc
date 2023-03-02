from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from employees.models import Employee
import json
from django.views.decorators.csrf import csrf_exempt


#json response
# def members(request):
#     return JsonResponse({'id':'1'})


#basic html response
# def members(request):
#     return HttpResponse("hello world!")

#basic html response with html template file
# def members(request):
#     template=loader.get_template('myfirst.html')
#     return HttpResponse(template.render())
@csrf_exempt
def add_members(request):
    if request.method=='POST':
        member=json.loads(request.body)
        a=Employee(firstname=member['name'],emp_id=member['id'])
        a.save()
    else:
        member = Employee(firstname='Emil', emp_id=1)
        member.save()
    mymembers = Employee.objects.all().values()
    template = loader.get_template('employees.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def del_members(request):
    member = Employee.objects.all()[0]
    member.delete()
    mymembers = Employee.objects.all().values()
    template = loader.get_template('employees.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))