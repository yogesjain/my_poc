import boto3



from django.http import JsonResponse

from my_poc.settings import DB_ENDPOINT

dynamodb=boto3.resource('dynamodb',endpoint_url=DB_ENDPOINT)
table= dynamodb.Table('employees')
def get_item(request, firstName):
    # table = dynamodb.Table('employees')

    print(table.item_count)
    response = table.get_item(
        # TableName='employees',
        Key={
            'firstName': firstName
        }
    )
    print(response)
    item = response.get('Item')
    if not item:
        return JsonResponse({'error': 'Item not found'}, status=404)
    data = {
        'firstName': item['firstName'],
        'lastName': item['lastName'],
        'empId': item['empId']
        # add more fields as needed
    }
    return JsonResponse(data)

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
# @csrf_exempt
# def add_members(request):
#     if request.method=='POST':
#         member=json.loads(request.body)
#         a=Employee(firstname=member['name'],emp_id=member['id'])
#         a.save()
#     else:
#         member = Employee(firstname='Emil', emp_id=1)
#         member.save()
#     mymembers = Employee.objects.all().values()
#     template = loader.get_template('employees.html')
#     context = {
#     'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))
#
# def del_members(request):
#     member = Employee.objects.all()[0]
#     member.delete()
#     mymembers = Employee.objects.all().values()
#     template = loader.get_template('employees.html')
#     context = {
#     'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))